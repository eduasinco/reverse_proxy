from django.db import models


class CompanyClient(models.Model):
    company_name = models.CharField(max_length=200, default='', null=True)
    is_active = models.BooleanField(default=True, null=True)


class ClientURL(models.Model):
    client = models.ForeignKey('CompanyClient', on_delete=models.CASCADE, default=None)
    formatted_url = models.CharField(max_length=1000, default='', null=True)
    is_open_for_cache = models.BooleanField(default=True, null=True)

