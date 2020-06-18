from rest_framework import serializers
from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id', )


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id', )

#
# class RecipeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         """:arg
#          user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#          title = models.CharField(max_length=255)
#          time_minutes = models.IntegerField()
#          price = models.DecimalField(decimal_places=2, max_digits=10)
#          link = models.CharField(max_length=255, blank=True)
#          ingredients = models.ManyToManyField('Ingredient')
#          tags = models.ManyToManyField('Tag')
#          """
#
#         ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
#         tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
#         model = Recipe
#         fields = ('id', 'user', 'title', 'time_minutes', 'price', 'link', 'ingredients', 'tags')
#         read_only_fields = ('id', )


class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'ingredients', 'tags', 'time_minutes', 'price',
            'link',
        )
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

