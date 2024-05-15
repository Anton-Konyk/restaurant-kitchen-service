from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook, DishType, Dish

COOK_FORMAT_URL = reverse("kitchen:cook-list")


class PublicCookTest(TestCase):
    def test_login_required(self):
        """
        Checking possibility for non-login user have access to cook-list
        working LoginRequiredMixin for CookDetailView
        :return:
        """
        res = self.client.get(COOK_FORMAT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateCookFormat(TestCase):
    def setUp(self) -> None:
        number_of_cooks = 9

        for cook_id in range(number_of_cooks):
            get_user_model().objects.create_user(
                username=f"Test-username {cook_id}",
                password=f"Test-001{cook_id}",
            )
        self.client.force_login(get_user_model().objects.get(pk=1))

    def test_retrieve_cook_formats(self):
        """
        Checking access login user to DriverListView page
        """
        response = self.client.get(COOK_FORMAT_URL)
        self.assertEqual(response.status_code, 200)
        cook_formats = get_user_model().objects.all()[:8]
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cook_formats),
        )
        # checking url path to kitchen/cook_list.html
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_pagination_cook_is_five(self):
        response = self.client.get(COOK_FORMAT_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["cook_list"]), 8)

    def test_lists_all_cooks(self):
        # Get second page and confirm it has (exactly) remaining 1 item
        response = self.client.get(COOK_FORMAT_URL + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["cook_list"]), 1)


class TestToggleAssignCookToDish(TestCase):
    def setUp(self):

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
        self.dish = Dish.objects.create(
                name="Test Dish",
                description="Test Dish description",
                price=0.01,
                dish_type=dish_type,
            )

    def test_toggle_assign_to_car(self):
        self.assertNotIn(self.user, self.dish.cooks.all())
        # response
        self.client.post(
            reverse("kitchen:toggle-cook-to-dish-assign",
                    kwargs={"pk": self.user.pk, "dish_id": self.dish.pk, "current_page": 1}
                    )
            )
        self.user.refresh_from_db()
        self.assertIn(self.user, self.dish.cooks.all())
        # response
        self.client.post(
            reverse("kitchen:toggle-cook-to-dish-assign",
                    kwargs={"pk": self.user.pk, "dish_id": self.dish.pk, "current_page": 1}
                    )
        )
        self.user.refresh_from_db()
        self.assertNotIn(self.user, self.dish.cooks.all())

    def test_toggle_assign_dish_to_cook_delete(self):
        self.user.dishes.add(self.dish.pk)
        # response
        self.client.post(
            reverse("kitchen:toggle-dish-to-cook-delete",
                    kwargs={"pk": self.dish.pk, "cook_id": self.user.pk}
                    )
            )
        self.user.refresh_from_db()
        self.assertNotIn(self.user, self.dish.cooks.all())
