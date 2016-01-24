from django.views.generic import View
from django.template.response import TemplateResponse

from django_datatables_view.base_datatable_view import BaseDatatableView

from . import forms, models


class Search(View):
    " Main view of messages "
    template_name = "chatalert/search.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return TemplateResponse(request, self.template_name, context=context)


class SearchJSON(BaseDatatableView):
    " JSON view backing datatable "
    model = models.Message
    columns = ['label_user', 'creation_datetime', 'text']
    order_columns = columns
    max_display_length = 1000

    def filter_queryset(self, qs):
        form = forms.Search(dict(regex=self.request.GET.get('search[value]')))
        return form.filter(qs)

    def render_column(self, row, column):
        if column == 'label_user':
            fake_form = forms.RowLabel(instance=row)
            return "<form>%s</form>" % (fake_form['label_user'],)
            
        return super(SearchJSON, self).render_column(row, column)
