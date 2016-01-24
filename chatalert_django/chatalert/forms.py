from django import forms

from . import models

class Search(forms.Form):
    regex = forms.CharField(required=False)

    def filter(self, queryset):
        " Filter given querset to match our search "
        if not self.is_valid():
            raise "Assert"

        regex = self.cleaned_data['regex']

        return (queryset.filter(creation_datetime__iregex=regex) |
                queryset.filter(message_type__iregex=regex) |
                queryset.filter(source__iregex=regex) |
                queryset.filter(url__iregex=regex) |
                queryset.filter(text__iregex=regex) |
                queryset.filter(author__iregex=regex) |
                queryset.filter(author_age__iregex=regex) |
                queryset.filter(city_state__iregex=regex) |
                queryset.filter(lat__iregex=regex) |
                queryset.filter(lng__iregex=regex) |
                queryset.filter(phone_number__iregex=regex) |
                queryset.filter(post_id__iregex=regex))

    def search(self):
        return self.filter(models.Message.objects)


class RowLabel(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['label_user']

    def __init__(self, *args, **kwargs):
        super(RowLabel, self).__init__(*args, **kwargs)
        if not self.is_bound:
            if "label_user" not in self.initial:
                self.initial["label_user"] = self.instance["label_auto"]
