from django.views.generic import *
from django.db.models import *
from django.forms import *
from roast.models import *
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from sales.models import *
from inventory.models import *

def main_view(req):
    return HttpResponseRedirect(reverse('batch_list'))

class OrderBatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = [ 'bag', 'initial_weight' ]

class BatchCreate(CreateView):
    model = Batch
    template_name = 'roast/detail_form.html'
    success_url = reverse_lazy('batch_list')

    def get_form(self, form_class):
        form = super(BatchCreate,self).get_form(form_class) #instantiate using parent
        form.fields['bag'].queryset = CoffeeBag.objects.annotate(used=Sum('batch__initial_weight')).filter(Q(used__lt=F('weight')) | Q(used__isnull=True))
        return form

class OrderBatchCreate(BatchCreate):
    form_class = OrderBatchForm

    def get_initial(self):
        return { 'order': self.kwargs['order_pk'] }

    def get_success_url(self):
        return reverse_lazy('order_detail', kwargs = { 'pk': self.kwargs['order_pk'] })
