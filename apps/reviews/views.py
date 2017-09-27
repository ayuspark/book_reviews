# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.
def index(request):
    all_reviews = Review.objects.all().order_by(
        '-created_date')[:5]
    books_with_reviews = Book.objects.exclude(reviews__isnull=True)
    context = {
        'all_reviews': all_reviews,
        'books_with_reviews': books_with_reviews,
    }
    return render(request, 'reviews/index.html', context)


def book_detail(request, book_id):
    # book_query = Book.objects.get(pk=book_id)
    book_query = get_object_or_404(Book, pk=book_id)
    context = {
        'book_query': book_query,
        'book_id': book_id,
    }
    return render(request, 'reviews/book_detail.html', context)


@login_required(login_url='/')
def add_book(request):
    book_form = BookForm(request.POST or None)
    select_author_form = SelectAuthorForm(request.POST or None)
    review_form = ReviewForm(request.POST or None)
    context = {
        'book_form': book_form,
        'select_author_form': select_author_form,
        'review_form': review_form,
    }
    if book_form.is_valid() and select_author_form.is_valid() and review_form.is_valid():
        # check if book exists
        new_book = book_form.save(commit=False)
        try:
            book_query = Book.objects.get(title__iexact=new_book.title)
        except Book.DoesNotExist:
            book_form.save()
            book_query = Book.objects.get(title__iexact=new_book.title)

        # query author to add to the new book
        author_object = select_author_form.cleaned_data.get('choose_author')
        first_name = author_object.first_name
        last_name = author_object.last_name
        author_query = Author.objects.filter(first_name__iexact=first_name).filter(last_name__iexact=last_name)
        # add author to book
        book_query.authors.add(author_query.first())
        
        # add review
        new_review = review_form.save(commit=False)
        new_review.user = get_object_or_404(User, pk=request.user.id)
        new_review.book = book_query
        new_review.save()

        book_id = book_query.id
        return redirect('reviews:book_detail', book_id=book_id)
    return render(request, 'reviews/add_new.html', context)


def user_detail(request, user_id):
    pass


@login_required(login_url='/')
def review_delete(request, book_id, review_id):
    Review.objects.get(pk=review_id).delete()
    return redirect('reviews:book_detail', book_id=book_id)
