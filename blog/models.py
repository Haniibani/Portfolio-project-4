from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'))
GLUTENFREE = "Glutenfree"
LACTOSEFREE = "Lactosefree"
NORMAL = "Normal"
VEGAN = "Vegan"
NUTFREE = "Nutfree"
TAGS = [
    (GLUTENFREE, "Glutenfree"),
    (LACTOSEFREE, "Lactosefree"),
    (NORMAL, "Normal"),
    (VEGAN, "Vegan"),
    (NUTFREE, "Nutfree"),
]


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    tag = models.CharField(max_length=100, choices=TAGS, default=NORMAL)
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    estimated_time = models.IntegerField('Estimated time')
    instructions = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    amount = models.IntegerField()
