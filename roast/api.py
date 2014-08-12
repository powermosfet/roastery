from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from roast.models import Batch, RoastPoint, Event

class RoastpointResource(ModelResource):
    batch = fields.ForeignKey('roast.api.BatchResource', 'batch')

    class Meta:
        queryset = RoastPoint.objects.all()
        resource_name = 'roastpoint'
        authorization = Authorization()

class BatchResource(ModelResource):
    roastpoint_set = fields.ToManyField('roast.api.RoastpointResource', 'roastpoint_set')

    class Meta:
        queryset = Batch.objects.all()
        resource_name = 'batch'
        authorization = Authorization()

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        authorization = Authorization()
