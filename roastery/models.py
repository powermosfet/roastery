class SelflinkMixin(object):
    def selflink(self):
        app = self.__module__.replace('.models', '')
        model = self.__class__.__name__.lower()
        return u'<a href="/admin/{0}/{1}/{2}/">{3}</a>'.format(app, model, self.pk, self.__unicode__())
    selflink.allow_tags = True
