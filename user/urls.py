from django.urls import path
from .views import UserCreate,UserLoginView

urlpatterns = [
    path("register/", UserCreate.as_view(), name="user-create"),
    path("login/", UserLoginView.as_view(), name="token_obtain_pair"),
]
