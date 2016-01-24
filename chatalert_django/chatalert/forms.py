from django import forms
from .models import Message

class SearchForm(forms.Form):
    regex = forms.CharField(required=False)

    def search(self):
        if not self.is_valid():
            raise "Assert"

        regex = self.cleaned_data['regex']

        return (Message.objects.filter(creation_datetime__iregex=regex) |
                Message.objects.filter(message_type__iregex=regex) |
                Message.objects.filter(source__iregex=regex) |
                Message.objects.filter(url__iregex=regex) |
                Message.objects.filter(text__iregex=regex) |
                Message.objects.filter(author__iregex=regex) |
                Message.objects.filter(author_age__iregex=regex) |
                Message.objects.filter(city_state__iregex=regex) |
                Message.objects.filter(lat__iregex=regex) |
                Message.objects.filter(lng__iregex=regex) |
                Message.objects.filter(phone_number__iregex=regex) |
                Message.objects.filter(post_id__iregex=regex))
