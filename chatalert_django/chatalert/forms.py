import uuid

from django import forms

from . import models
from chosen import forms as chosenforms

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
                queryset.filter(comments__iregex=regex) |
                queryset.filter(post_id__iregex=regex))


class RowEdit(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['label_user', 'comments']
        widgets = {'label_user': chosenforms.ChosenSelect,
                   'comments': forms.Textarea(attrs=dict(rows=3))}

    def clean(self):
        " Don't change fields that weren't specified "
        cleaned_data = super(RowEdit, self).clean()
        for key in ['label_user', 'comments']:
            if not cleaned_data[key]:
                del cleaned_data[key]
        return cleaned_data

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('auto_id', "id_" + str(uuid.uuid4()) + "_%s")
        super(RowEdit, self).__init__(*args, **kwargs)
        if not self.is_bound:
            if "label_user" not in self.initial:
                self.initial["label_user"] = self.instance["label_auto"]
