from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.horses import views

urlpatterns = [

    path('registration/', views.UserCreate.as_view()),

    # refresh token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('image/', views.HorseImageListCreate.as_view()),
    path('image/<str:pk>/', views.HorseImageRetrieveUpdateDestroyAPIView.as_view()),

    path('profile/<str:pk>/', views.HorseProfileRetrieveUpdateDestroyAPIView.as_view()),
    path('profile/', views.HorseProfileListCreate.as_view()),

    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('login/', views.UserLoginView.as_view()),
]
