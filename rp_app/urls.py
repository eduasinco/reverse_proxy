from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('my_active_urls/<str:client>/', views.ActiveClientURL.as_view()),
    path('my_inactive_urls/<str:client>/', views.InactiveClientURL.as_view()),
    path('activate_url/<int:pk>/', csrf_exempt(views.ActivateURL.as_view())),
    path('delete_from_cache/<int:pk>/', csrf_exempt(views.DeleteURLFromCache.as_view())),
]
