from django.views.generic import TemplateView,CreateView, DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models
import proj

class HomePageView(TemplateView):
    template_name = 'databook/home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')
        if search_by in ['data','day'] and query:
            if search_by == 'day':
                day = models.Date.objects.filter(day=query)
            else:
                day = models.Date.objects.filter(numbers__data=query)
            context["day"] = day
            return context
        context["day"] = models.Date.objects.all()
        return context



class AddInfoFormView(CreateView):
    template_name = 'databook/add_info.html'
    form_class = forms.CreateDateFrom
    success_url = reverse_lazy('home')
    def get_success_url(self) ->str:
        info_data = self.request.POST.get('numbers')
        for info_data in info_data.split('\n'):
            models.Info.objects.create(data=info_data,time=self.object)
        return super().get_success_url()


class DeleteInfoView(DeleteView):
    model = models.Date
    template_name = 'databook/delete_Date.html'
    success_url = reverse_lazy('home')
