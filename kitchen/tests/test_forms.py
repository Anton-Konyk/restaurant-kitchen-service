from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.forms import CookCreationForm, DishCreationForm
from kitchen.models import Ingredient, DishType


class FormTests(TestCase):
    def test_cook_creation_form_with_first_last_name_prax_years(self):
        """
        Checking valid form
        """
        form_data = {
            "username": "new_user",
            "first_name": "Test first",
            "last_name": "Test last",
            "prax_years": 1001,
            "password1": "user12test",
            "password2": "user12test",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class DishCreationFormTest(TestCase):
    def test_create_dish_price_not_negative(self):
        """
        Checking valid price field. It's not a negative value.
        :return:
        """
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test1234",
            prax_years=1001,
        )
        ingredient = Ingredient.objects.create(
            name="Test ingredient"
        )
        dish_type = DishType.objects.create(
            name="Test Dish Type"
        )

        form_data = {
            "name": "Test Dish",
            "description": "Test Dish description",
            "dish_type": dish_type.pk,
            "cooks": [self.user.pk],
            "ingredients": [ingredient.pk],
            "price": -0.01,
        }
        form = DishCreationForm(data=form_data)
        self.assertTrue(not form.is_valid())
