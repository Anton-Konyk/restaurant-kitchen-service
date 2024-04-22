from django.urls import path

from kitchen import views
from kitchen.views import (
    index,
    UserPasswordResetView,
    UserLoginView,
    UserPasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetDoneView,
    UserPasswordResetConfirmView,
    PasswordResetCompleteView,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("accounts/login/", UserLoginView.as_view(), name="login"),
    path("accounts/logout/", views.logout_view, name="logout"),
    path("accounts/password-change/", UserPasswordChangeView.as_view(), name="password_change"),
    path("accounts/password-change-done/", PasswordChangeDoneView.as_view(
        template_name="accounts/password_change_done.html"
    ), name="password_change_done"),
    path("accounts/password-reset/", UserPasswordResetView.as_view(), name="password_reset"),
    path("accounts/password-reset-done/", PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"
    ), name="password_reset_done"),
    path("accounts/password-reset-confirm/<uidb64>/<token>/",
         UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("accounts/password-reset-complete/", PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_complete.html"
    ), name="password_reset_complete"),
    path("accounts/register/", views.register, name="register"),

    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(),name="ingredient-delete"),

    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(),name="dish-type-delete"),
]

app_name = "kitchen"
