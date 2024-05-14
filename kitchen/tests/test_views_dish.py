from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType

DISH_INGREDIENT_FORMAT_URL = reverse("kitchen:dish-list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        """
        Checking possibility for non-login user have access to dish-list
        working LoginRequiredMixin for DishListView
        :return:
        """
        res = self.client.get(DISH_INGREDIENT_FORMAT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishFormat(TestCase):
    def setUp(self) -> None:
        number_of_ingredients = 10

        self.user = get_user_model().objects.create_user(
            username="test1",
            password="test12345",
            first_name="test_first1",
            last_name="test_last1",
        )
        self.client.force_login(self.user)
        dish_type = DishType.objects.create(
            name="Test Dish Type"
        )
        for dish_id in range(number_of_ingredients):
            dish = Dish.objects.create(
                name=f"Test Dish {dish_id}",
                description="Test Dish description",
                price=0.01,
                dish_type=dish_type,
         )

    def test_retrieve_dish_formats(self):
        """
        Checking access login user to DishListView page
        """
        response = self.client.get(DISH_INGREDIENT_FORMAT_URL)
        self.assertEqual(response.status_code, 200)
        dish_formats = Dish.objects.all()[:8]
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dish_formats),
        )
        # checking url path to kitchen/dish_list.html
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_pagination_dish_is_eight(self):
        response = self.client.get(DISH_INGREDIENT_FORMAT_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["dish_list"]), 8)

    def test_lists_all_dish(self):
        # Get second page and confirm it has (exactly) remaining 2 items
        response = self.client.get(DISH_INGREDIENT_FORMAT_URL + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["dish_list"]), 2)
