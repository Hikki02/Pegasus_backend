from django.urls import path
from .views import UserMVC, DownloadVCF

plural = {
    'get': 'list'
}

single = {
    'get': 'retrieve',
    'delete': 'destroy',
    'patch': 'update',
    'post': 'create'
}

urlpatterns = [
    path('all/', UserMVC.as_view(plural)),
    path('<slug:unique_id>/', UserMVC.as_view(single)),
    path('download/<slug:unique_id>/', DownloadVCF.as_view())
]