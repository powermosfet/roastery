from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from inventory.models import Variety

class VarietyResource(ModelResource):
    class Meta:
        queryset = Variety.objects.all()
        resource_name = 'variety'
        authorization = Authorization()
