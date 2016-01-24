from django.views.generic import View
from django.template.response import TemplateResponse


from .forms import SearchForm


class Search(View):
    template_name = "chatalert/search.html"

    def get(self, request, *args, **kwargs):
        context = {}

        search_form = SearchForm(request.GET)
        search_results = search_form.search() if search_form.is_valid() else []

        context = dict(search_results=search_results,
                       search_form=search_form)

        return TemplateResponse(request, self.template_name, context=context)
