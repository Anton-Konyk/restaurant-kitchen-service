from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
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

    def test_prax_years_listed(self):
        """
        Test that user's prax years is in list_display on cook admin page
        :return:
        """
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.prax_years)

    def test_cook_detail_prax_years_listed(self):
        """
        Test that user's prax years is in on cook detail admin page
        :return:
        """
        url = reverse("admin:kitchen_cook_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertContains(res, self.user.prax_years)

    def test_cook_add_prax_years_listed(self):
        """
        Test that user's prax years is in on cook add admin page
        :return:
        """
        url = reverse("admin:kitchen_cook_add")
        res = self.client.get(url)

        self.assertContains(res, "prax_years")
