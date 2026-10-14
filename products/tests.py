from django.test import TestCase
from django.urls import reverse
from .models import Category, Product


class ProductTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            title="Digital",
            slug="digital"
        )

        self.product = Product.objects.create(
            category=self.category,
            title="Mouse",
            slug="mouse",
            description="Gaming Mouse",
            image="products/mouse.jpg",
            price=200000,
            stock=10
        )

    def test_product_list(self):
        url = reverse("shop") # /shop
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200) # if response.status_code == 200:
        self.assertEqual(len(response.data), 1)

    def test_product_detail(self):
        url = reverse("product-item", args=["mouse"])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Mouse")

    def test_product_not_found(self):
        url = reverse("product-item", args=["invalid"])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
