from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import *


User = get_user_model()


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        # manually fill in other fields upon form submit





# class SignInForm(forms.Form):
#     email = forms.EmailField()
#     psw = forms.CharField(widget=forms.PasswordInput,
#                           label='Password')


# class RegisterForm(forms.ModelForm):
#     psw = forms.CharField(widget=forms.PasswordInput,
#                           label='Password',)
#     confirm_psw = forms.CharField(widget=forms.PasswordInput,
#                                   label='Confirm Password',)

#     class Meta:
#         model = MyUser
#         exclude = ['is_admin']

#     def clean(self):
#         cleaned_data = super(RegisterForm, self).clean()
#         psw = cleaned_data.get('psw')
#         confirm_psw = cleaned_data.get('confirm_psw')

#         if psw != confirm_psw:
#             msg = 'Password does not match'
#             return self.add_error('confirm_psw', msg)


# class MessageForm(forms.ModelForm):

#     class Meta:
#         model = Message
#         fields = ('msg',)
#         labels = {
#             'msg': '',
#         }
#         widgets = {
#             'msg': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
#         }
#         # manually fill in other fields upon form submit


# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ('comment',)
#         widgets = {
#             'comment': forms.Textarea(attrs={'class': 'form-control',
#                                              'rows': '1',
#                                              'id': '', }),
#         }
#         # manually fill in other fields upon form submit
