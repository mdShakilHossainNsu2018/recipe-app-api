from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import User, Tag, Ingredient, Recipe
from unittest.mock import patch
from core import models


def simple_user(email='test@gmail.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_with_email_successfully(self):
        email = 'test@gmail.com'
        password = 'testpass'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        # print("user.email")
        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email_field(self):
        email = 'shakil@GMAIL.com'

        user = get_user_model().objects.create_user(email=email, password='passtest')
        # print('running as')

        self.assertEqual(user.email, email.lower())

    def test_email_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'something')

    def test_create_supper_user(self):
        user = get_user_model().objects.create_superuser('shakil@gmail.com', 'simpleTest')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        tag = Tag.objects.create(
            user=simple_user(),
            name='Vegan',
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(user=simple_user(), name='Banana')
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        recipe = Recipe.objects.create(user=simple_user(),
                                       title="Test Title for Recipe Model",
                                       time_minutes=5,
                                       price=5.00)
        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_the_recipe_file_name_uuid(self, mock_uuid):
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')
        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
