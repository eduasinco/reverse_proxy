from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rp_app.serializers import ClientURLSerializer
from .models import ClientURL
from django.http import Http404
from django.core.cache import cache


class ActiveClientURL(APIView):

    def get(self, request, client, format=None):
        urls = ClientURL.objects.filter(client__company_name=client, is_open_for_cache=True)
        serializer = ClientURLSerializer(urls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InactiveClientURL(APIView):
    def get(self, request, client, format=None):
        urls = ClientURL.objects.filter(client__company_name=client, is_open_for_cache=False)
        serializer = ClientURLSerializer(urls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActivateURL(APIView):
    def get_object(self, pk):
        try:
            return ClientURL.objects.get(pk=pk)
        except ClientURL.DoesNotExist:
            raise Http404

    def patch(self, request, pk, format=None):
        url = self.get_object(pk)
        serializer = ClientURLSerializer(url, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteURLFromCache(APIView):
    def get_object(self, pk):
        try:
            return ClientURL.objects.get(pk=pk)
        except ClientURL.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        url = self.get_object(pk)
        cache.delete(url.formatted_url)
        return Response({}, status=status.HTTP_200_OK)
