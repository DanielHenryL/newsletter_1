from django import forms
from newsletters.models import Newsletter

class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('name','subject','body','email','status')