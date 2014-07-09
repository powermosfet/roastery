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
 
    def get_success_url(self):
        return reverse('order_edit', kwargs={'pk': self.object.order.pk})

class BatchAdd(FormMixin, CreateView):
    model = Batch
    template_name = 'form.html'
    
    def get_success_url(self):
        return reverse('order_edit', kwargs={'pk': self.object.order.pk})

    def get_initial(self, *args, **kwargs):
        i = super(BatchAdd, self).get_initial(*args, **kwargs)
        if 'order' in self.request.GET.keys():
            i['order'] = self.request.GET['order']
        return i

class BatchEdit(FormMixin, UpdateView):
    model = Batch
    template_name = 'form.html'
    
    def get_success_url(self):
        return reverse('order_edit', kwargs={'pk': self.object.order.pk})
