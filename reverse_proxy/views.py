from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http import HttpResponse
import requests
from rp_app.models import CompanyClient, ClientURL
from .settings import CACHE_TIME_LIMIT
from django.db import models


@cache_page(CACHE_TIME_LIMIT)
def generic_caching_view(request):
    link = request.build_absolute_uri()
    f = requests.get(link)
    return HttpResponse(f.text)


def manual_caching_view(request):
    link = request.build_absolute_uri()
    try:
        client_url = ClientURL.objects.get(formatted_url=link)
    except models.ObjectDoesNotExist:
        client_name = request.headers['Host']
        try:
            client = CompanyClient.objects.get(company_name=client_name)
        except models.ObjectDoesNotExist:
            client = CompanyClient(
                company_name=client_name,
                is_active=True
            )
            client.save()

        client_url = ClientURL(
            client=client,
            formatted_url=link,
        )
        client_url.save()

    if client_url.client.is_active and client_url.is_open_for_cache and cache.get(link):
        return HttpResponse(cache.get(link))
    else:
        f = requests.get(link)
        max_age = 0
        no_cache = False
        headers = f.headers["Cache-Control"].split(',')
        for h in headers:
            if "max-age" in h:
                ma = h.split('=')
                max_age = int(ma[1])
            if "no-cache" in h:
                no_cache = True

        if no_cache:
            return HttpResponse(f.text)

        cache.set(link, f.text, max_age)
        return HttpResponse(f.text)


@cache_page(CACHE_TIME_LIMIT)
def test_caching_view(request):
    f = requests.get("https://www.example.com/")
    return HttpResponse(f.text)


