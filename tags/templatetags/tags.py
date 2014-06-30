from django import template
import django

register = template.Library()

@register.simple_tag
def navbar():
    names = django.conf.settings.INSTALLED_APPS
    modules = []
    items = []
    for name in [ '{}.views'.format(x) for x in names ]:
        try:
            modules.append(__import__(name))
        except ImportError as e:
            print name, type(e), e
    for m in modules:
        if hasattr(m.views, 'navbar_items'):
            items.extend(Menuitem(x) for x in m.views.navbar_items())
    c = template.Context({ 'items': items })
    t = template.loader.get_template('tags/navbar.html')
    return t.render(c)

@register.simple_tag
def menu_item(item):
    c = template.Context({ 'item': item, 'dropdown': hasattr(item, 'subitems') })
    t = template.loader.get_template('tags/menu_item.html')
    return t.render(c)

class Menuitem(object):
    def __init__(self, data):
        self.name = data[0]
        if type(data[1]) is list:
            self.subitems = [ Menuitem(x) for x in data[1] ]
        else:
            self.url = data[1]
