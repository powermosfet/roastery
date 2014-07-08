from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse, reverse_lazy 
from utilities.views import FormMixin

from roast.models import *

def navbar_items():
    return [
            ( 'Roast', [
                        ('Batches', reverse('batch_all')),
                        ] ),
                ]

class BatchList(ListView):
    model = Batch

class BatchOutstanding(BatchList):
    def get_queryset(self, *args, **kwargs):
        return Batch.objects.filter(done=False)


class BatchDelete(FormMixin, DeleteView):
    model = Batch  
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('batch_all')

class BatchAdd(FormMixin, CreateView):
    model = Batch
    template_name = 'form.html'
    
    def get_success_url(self, *args, **kwargs):
        return reverse('batch_all')

    def get_initial(self, *args, **kwargs):
        i = super(BatchAdd, self).get_initial(*args, **kwargs)
        if 'customer' in self.request.GET.keys():
            i['customer'] = self.request.GET['customer']
        return i

class BatchEdit(FormMixin, UpdateView):
    model = Batch
    template_name = 'sales/batch_form.html'
    success_url = reverse_lazy('batch_all')
