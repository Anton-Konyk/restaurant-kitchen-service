from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Ingredient, DishType, Dish


class ModelsTests(TestCase):
    def test_ingredient_format_str(self):
        ingredient_format = Ingredient.objects.create(
            name="test_name",
        )
        self.assertEqual(
            str(ingredient_format),
            ingredient_format.name
        )

    def test_dish_type_format_str(self):
        dish_type_format = DishType.objects.create(
            name="test_name",
        )
        self.assertEqual(
            str(dish_type_format),
            dish_type_format.name
        )

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="new_user",
            first_name="Test first",
            last_name="Test last",
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_format_str(self):
        dish_type = DishType.objects.create(
            name="Test Dish Type"
        )
        dish_format = Dish.objects.create(
            name="Test Dish",
            description="Test Dish description",
            price=0.01,
            dish_type=dish_type,
         )
        self.assertEqual(
            str(dish_format),
            dish_format.name
        )

    def test_create_cook_with_license_number(self):
        prax_years = 1001
        username = "new_user"
        password = "asop123q1"
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            prax_years=prax_years,
        )
        self.assertEqual(cook.prax_years, prax_years)
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))

    def test_get_absolute_url_ingredient(self):
        ingredient = Ingredient.objects.create(
            name="test_name",
        )
        self.assertEqual(
            ingredient.get_absolute_url(),
            "/ingredients/1/"
        )

    def test_get_absolute_url_dish_type(self):
        dish_type = DishType.objects.create(
            name="test_name",
        )
        self.assertEqual(
            dish_type.get_absolute_url(),
            "/dish-types/1/"
        )

    def test_get_absolute_url_cook(self):
        cook = get_user_model().objects.create_user(
            username="test",
            password="test12345",
        )
        self.assertEqual(
            cook.get_absolute_url(),
            "/cooks/1/"
        )

    def test_get_absolute_url_dish(self):
        dish_type = DishType.objects.create(
            name="Test Dish Type"
        )
        dish = Dish.objects.create(
            name="Test Dish",
            description="Test Dish description",
            dish_type=dish_type,
            price=1001,
        )
        self.assertEqual(
            dish.get_absolute_url(),
            "/dishes/1/"
        )
