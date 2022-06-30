from django import forms
from .models import NewsletterUser


class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model= NewsletterUser
        fields = ('email',)
