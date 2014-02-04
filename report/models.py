from django.db import models
from django.contrib.auth.models import Group, User
from config.report_config import PARAM_TYPES

# Create your models here.


class BaseModel(models.Model):
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_adder", on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_editor", on_delete=models.PROTECT)
    modified_date = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Portfolio(BaseModel):
    """
    Name of  the different Portfolios
    """
    name = models.CharField(max_length=100, unique=True)
    groups = models.ManyToManyField(Group, blank=True, null=True)


class QueryParameter(BaseModel):
    parameter_name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=20, choices=PARAM_TYPES, default="text")
    values = models.TextField()
    description = models.TextField(null=True)


class DBConnection(BaseModel):
    connection_name = models.CharField(max_length=50, unique=True)
    host = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    description = models.TextField(null=True)


class Report(BaseModel):
    report_name = models.CharField(max_length=50, unique=True)
    query = models.TextField()
    db = models.ForeignKey(DBConnection, on_delete=models.PROTECT)
    description = models.TextField(null=True)
    groups = models.ManyToManyField(Group, blank=True, null=True)
    users = models.ManyToManyField(User, blank=True, null=True)


