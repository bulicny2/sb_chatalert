import logging

from django.views.generic import View
from django.template.response import TemplateResponse, HttpResponse
from django.core.urlresolvers import reverse

from django_datatables_view.base_datatable_view import BaseDatatableView

from . import forms, models


logger = logging.getLogger(__name__)


class Search(View):
    " Main view of messages "
    template_name = "chatalert/search.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return TemplateResponse(request, self.template_name, context=context)


class SearchJSON(BaseDatatableView):
    " JSON view backing datatable "
    model = models.Message
    columns = ['label_user', 'creation_datetime', 'text', 'comments']
    order_columns = columns
    max_display_length = 1000

    def filter_queryset(self, qs):
        form = forms.Search(dict(regex=self.request.GET.get('search[value]')))
        return form.filter(qs)

    def render_column(self, row, column):
        fake_form = forms.RowEdit(instance=row)

        if column in {'label_user', 'comments'}:
            return ("<form method=POST target='hidden-iframe' action=%s>%s</form>" %
                    (reverse('chatalert_search_edit', kwargs=dict(pk=row.pk)),
                     fake_form[column]))
        else:
            return super(SearchJSON, self).render_column(row, column)


class SearchEdit(View):
    def post(self, request, pk):
        instance = models.Message.objects.get(pk=pk)
        form = forms.RowEdit(request.POST, instance=instance)
        if not form.is_valid():
            import pdb; pdb.set_trace()
            raise "Assert"
        try:
            form.save()
            logger.info("Saved edit to %s", pk)
        except:
            import traceback; traceback.print_exc();
            import pdb; pdb.post_mortem();
        return HttpResponse()
