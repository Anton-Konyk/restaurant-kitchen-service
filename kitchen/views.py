from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render, redirect

from kitchen.forms import UserLoginForm, UserPasswordResetForm, RegistrationForm
from kitchen.models import Ingredient, DishType, Cook, Dish


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


class UserLoginView(LoginView):
  template_name = "accounts/sign-in.html"
  form_class = UserLoginForm


class UserPasswordResetView(PasswordResetView):
  template_name = "accounts/password_reset.html"
  form_class = UserPasswordResetForm


def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print("Account created successfully!")
      return redirect('/accounts/login')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/sign-up.html', context)
