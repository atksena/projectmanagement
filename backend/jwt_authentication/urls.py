from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import ExampleView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    # path('login/', obtain_jwt_token),
    # path('refresh-token/', refresh_jwt_token),
    path('example/', ExampleView.as_view())
]
