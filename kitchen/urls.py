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
    CookListView,
    CookCreateView,
    CookDetailView,
    CookDeleteView,
    toggle_assign_dish_to_cook,
    CookUpdateView,
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishDetailView,
    toggle_assign_cook_to_dish,
    IngredientDetailView,
    DishTypeDetailView,
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
    path("ingredients/<int:pk>/", IngredientDetailView.as_view(), name="ingredient-detail"),

    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(),name="dish-type-delete"),
    path("dish-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),

    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("cooks/<int:pk>/<int:cook_id>/toggle-assign/", toggle_assign_dish_to_cook, name="toggle-dish-to-cook-assign"),

    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(),name="dish-delete"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/<int:pk>/<int:dish_id>/toggle-assign/", toggle_assign_cook_to_dish, name="toggle-cook-to-dish-assign"),
]

app_name = "kitchen"
