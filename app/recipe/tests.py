# from django.test import TestCase
#
# # Create your tests here.
# from rest_framework import status
#
# from core.models import Recipe
# from recipe.test_recipe_api import RECIPES_URL
#
#
# class TestApiRecipe(TestCase):
#
#     def test_create_basic_recipe(self):
#         """Test creating recipe"""
#         payload = {
#             'title': 'Test recipe',
#             'time_minutes': 30,
#             'price': 10.00,
#         }
#
#
#
#         res = self.client.post(RECIPES_URL, payload)
#
#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)
#
#         recipe = Recipe.objects.get(id=res.data['id'])
#         for key in payload.keys():
#             self.assertEqual(payload[key], getattr(recipe, key))
