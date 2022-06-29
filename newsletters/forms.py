from django import forms
from .models import NewsletterUser,Newsletter


class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model= NewsletterUser
        fields = ('email',)

class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('name','subject','body','email',)