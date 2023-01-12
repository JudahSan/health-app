from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Food(models.Model):
  def __str__(self):
    return self.name

  name = models.CharField(max_length=100)
  carbs = models.FloatField()
  protein = models.FloatField()
  fats = models.FloatField()
  calories = models.IntegerField()

# store items consumed by users
class Consume(models.Model):

  # def __str__(self):
  #   return self.user

  # Consumer
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  # Fk associated 2 models together
  food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)