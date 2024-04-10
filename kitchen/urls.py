from django.urls import path

from kitchen import views
from kitchen.views import index, UserPasswordResetView, UserLoginView

urlpatterns = [
    path("", index, name="index"),
    path("accounts/login/", UserLoginView.as_view(), name="login"),
    path("accounts/password-reset/", UserPasswordResetView.as_view(), name="password_reset"),
    path("accounts/register/", views.register, name="register"),
]

app_name = "kitchen"
