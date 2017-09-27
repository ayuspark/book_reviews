from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout


User = get_user_model()


class UserLoginForm(forms.Form):
    """
    " use the following to use EMAIL to sign in
    ' email = forms.EmailField()
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *arg, **kwargs):
        """"
        " email = self.cleaned_data.get('email')
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            """
            " if email and password:
            " username = User.objects.get(email=email).username
            """
            user_auth = authenticate(username=username, password=password)
            user_query = User.objects.filter(username=username)
            if not user_query.exists():
                raise forms.ValidationError('User does not exist.')
            if not user_auth:
                raise forms.ValidationError('Somthing is wrong with your username or password.')
            # if not user.check_password(password):
            #     raise forms.ValidationError('Somthing is wrong with your username or password.')
            if not user_auth.is_active:
                raise forms.ValidationError('This user is no longer active')
        return super(UserLoginForm, self).clean()


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, 
                               min_length=8,
                               help_text='At least 8 digits long.')
    confirm_password = forms.CharField(widget=forms.PasswordInput,
                                       label='Confirm Password',)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
        ]
    
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        email = self.cleaned_data.get('email')
        if password != confirm_password:
            raise forms.ValidationError('Passwords must match.')
        email_query = User.objects.filter(email=email)
        if email_query.exists():
            raise forms.ValidationError('Email already exists.')
        return super(UserRegistrationForm, self).clean()
    
