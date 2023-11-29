from django.urls import path, include
from .views import CustomLoginView

urlpatterns = [    
    path("login/", CustomLoginView.as_view(), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
]
