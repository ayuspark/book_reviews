# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from .models import *


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
    pass


def user_detail(request, user_id):
    pass


def add_book(request):
    pass