
class FormMixin(object):
    def get_context_data(self, *args, **kwargs):
        name = self.model.__name__.lower()
        kwargs['edit_view'] = '{}_edit'.format(name)
        kwargs['add_view'] = '{}_add'.format(name)
        kwargs['delete_view'] = '{}_delete'.format(name)
        return super(FormMixin, self).get_context_data(*args, **kwargs)
