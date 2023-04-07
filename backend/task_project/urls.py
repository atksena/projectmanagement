from django.urls import path, include

urlpatterns = [
    path('api/', include('task.urls')),
    path('api/', include('jwt_authentication.urls'))
]