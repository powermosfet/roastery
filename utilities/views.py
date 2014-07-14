from django.shortcuts import render_to_response

def direct(template):
    def direct_view(r, *args, **kwargs):
        return render_to_response(template, kwargs)
    return direct_view

class FormMixin(object):
    def get_context_data(self, *args, **kwargs):
        name = self.model.__name__
        name_lower = name.lower()
        kwargs['modelname'] = name
        kwargs['edit_view'] = '{}_edit'.format(name_lower)
        kwargs['add_view'] = '{}_add'.format(name_lower)
        kwargs['delete_view'] = '{}_delete'.format(name_lower)
        return super(FormMixin, self).get_context_data(*args, **kwargs)
