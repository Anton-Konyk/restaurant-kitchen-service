from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Ingredient


INGREDIENT_FORMAT_URL = reverse("kitchen:ingredient-list")


class PublicIngredientTest(TestCase):
    def test_login_required(self):
        """
        Checking possibility for non-login user have access to ingredient-list
        working LoginRequiredMixin for IngredientListView
        :return:
        """
        res = self.client.get(INGREDIENT_FORMAT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateIngredientFormat(TestCase):
    def setUp(self) -> None:
        number_of_ingredients = 10

        self.user = get_user_model().objects.create_user(
            username="test1",
            password="test12345",
            first_name="test_first1",
            last_name="test_last1",
        )
        self.client.force_login(self.user)

        for ingredient_id in range(number_of_ingredients):
            ingredient = Ingredient.objects.create(
                name=f"Test-name {ingredient_id}",
            )

    def test_retrieve_ingredient_formats(self):
        """
        Checking access login user to IngredientListView page
        """
        response = self.client.get(INGREDIENT_FORMAT_URL)
        self.assertEqual(response.status_code, 200)
        ingredient_formats = Ingredient.objects.all()[:8]
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(ingredient_formats),
        )
        # checking url path to kitchen/ingredient_list.html
        self.assertTemplateUsed(response, "kitchen/ingredient_list.html")

    def test_pagination_ingredient_is_eight(self):
        response = self.client.get(INGREDIENT_FORMAT_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["ingredient_list"]), 8)

    def test_lists_all_ingredient(self):
        # Get second page and confirm it has (exactly) remaining 2 items
        response = self.client.get(INGREDIENT_FORMAT_URL + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["ingredient_list"]), 2)
