from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView,
                                       PasswordResetView,
                                       PasswordChangeView,
                                       PasswordResetConfirmView,
                                       PasswordContextMixin,
                                       )
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import TemplateView
from django.utils.translation import gettext as _

from kitchen.forms import (UserLoginForm,
                           UserPasswordResetForm,
                           RegistrationForm,
                           UserPasswordChangeForm,
                           UserSetPasswordForm,
                           IngredientSearchForm,
                           CookSearchForm,
                           CookCreationForm,
                           CookForm,
                           DishSearchForm,
                           DishCreationForm,
                           )
from kitchen.models import Ingredient, DishType, Cook, Dish
from restaurant_kitchen_service import settings


@login_required
def index(request):
    """View function for the home page of the site."""

    num_ingredients = Ingredient.objects.count()
    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_ingredients": num_ingredients,
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    context_object_name = "ingredient_list"
    template_name = "kitchen/ingredient_list.html"
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = IngredientSearchForm(
            initial={"name": name}
        )
        context["search_text"] = name
        return context

    def get_queryset(self):
        queryset = super(IngredientListView, self).get_queryset()
        form = IngredientSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientDetailView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IngredientDetailView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = IngredientSearchForm(
            initial={"name": name}
        )
        context["search_text"] = name
        return context

    def get_queryset(self):
        ingredient_pk = self.kwargs["pk"]
        ingredient = get_object_or_404(Ingredient, pk=ingredient_pk)
        queryset = ingredient.dishes.all()
        form = IngredientSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = IngredientSearchForm(
            initial={"name": name}
        )
        context["search_text"] = name
        return context

    def get_queryset(self):
        queryset = super(DishTypeListView, self).get_queryset()
        form = IngredientSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    template_name = "kitchen/dish_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    template_name = "kitchen/dish_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDetailView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeDetailView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = IngredientSearchForm(
            initial={"name": name}
        )
        context["search_text"] = name
        return context

    def get_queryset(self):
        dish_type_pk = self.kwargs["pk"]
        dish_type = get_object_or_404(Ingredient, pk=dish_type_pk)
        queryset = dish_type.dishes.all()
        form = IngredientSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )
        context["search_text"] = username
        return context

    def get_queryset(self):
        queryset = super(CookListView, self).get_queryset()
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDetailView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookDetailView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )
        context["search_text"] = name
        return context

    def get_queryset(self):
        cook_pk = self.kwargs["pk"]
        cook = get_object_or_404(Cook, pk=cook_pk)
        queryset = cook.dishes.all()
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookForm
    success_url = reverse_lazy("kitchen:cook-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        cook_instance = form.instance
        dishes = form.cleaned_data['dishes']
        cook_instance.dishes.clear()
        for dish in dishes:
            cook_instance.dishes.add(dish)
        return response


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "kitchen/dish_list.html"
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )
        context["search_text"] = name
        return context

    def get_queryset(self):
        queryset = super(DishListView, self).get_queryset()
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    template_name = "kitchen/dish_form.html"
    form_class = DishCreationForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    template_name = "kitchen/dish_form.html"
    form_class = DishCreationForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDetailView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishDetailView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"name": username}
        )
        context["search_text"] = username
        return context

    def get_queryset(self):
        dish_pk = self.kwargs["pk"]
        dish = get_object_or_404(Dish, pk=dish_pk)
        queryset = dish.cooks.all()
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class UserLoginView(LoginView):
    template_name = "accounts/sign-in.html"
    form_class = UserLoginForm


def logout_view(request):
    logout(request)
    return redirect('/accounts/login')


class UserPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset.html"
    form_class = UserPasswordResetForm


class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name = "registration/password_reset_done.html"
    title = _("Password reset sent")


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    form_class = UserSetPasswordForm


class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("kitchen:password_change_done")
    template_name = "accounts/password_change.html"
    form_class = UserPasswordChangeForm


class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = "registration/password_reset_complete.html"
    title = _("Password reset complete")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_url"] = resolve_url(settings.LOGIN_URL)
        return context


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = "accounts/password_change_done.html"
    title = _("Password change successful")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Account created successfully!")
            return redirect('/accounts/login')
        else:
            print("Registration failed!")
    else:
        form = RegistrationForm()

    context = {"form": form}
    return render(request, 'accounts/sign-up.html', context)


@login_required
def toggle_assign_dish_to_cook(request, pk, cook_id):
    cook = Cook.objects.get(id=cook_id)
    if (
        Dish.objects.get(id=pk) in cook.dishes.all()
    ):
        cook.dishes.remove(pk)
    # else:
    #     cook.dishes.add(pk)
    return HttpResponseRedirect(reverse_lazy(
        "kitchen:cook-detail",
        args=[cook.id])
    )


@login_required
def toggle_assign_cook_to_dish(request, pk, dish_id):
    dish = Dish.objects.get(id=dish_id)
    if (
        Cook.objects.get(id=pk) in dish.cooks.all()
    ):
        dish.cooks.remove(pk)
    return HttpResponseRedirect(reverse_lazy(
        "kitchen:dish-detail",
        args=[dish.id])
    )
