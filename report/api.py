__author__ = 'kamal.s'

from tastypie.resources import ModelResource
from django.contrib.auth.models import User

from .models import Portfolio


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name']
        allowed_methods = "get"


class PortfolioResource(ModelResource):
    class Meta:
        queryset = Portfolio.objects.all()
        print queryset
        resource_name = 'portfolio'
