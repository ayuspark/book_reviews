# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    title = models.TextField(max_length=140)
    

class Review(models.Model):
    rating = models.PositiveIntegerField(default=5, 
                                         validators=(MinValueValidator(1),
                                                     MaxValueValidator(5))
                                        )
    comment = models.TextField(max_length=140)
    user = models.ForeignKey(User, related_name='reviews')
    book = models.ForeignKey(Book, related_name='reviews')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.comment
    
    def update(self):
        self.update_date = timezone.now
        self.save()


