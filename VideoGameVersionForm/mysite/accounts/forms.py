from django import forms


class LoginForm(forms.Form): # This form will be used to authenticate users against the database.
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) # The PasswordInput widget is used to render the password HTML element. This will include type="password" in the HTML