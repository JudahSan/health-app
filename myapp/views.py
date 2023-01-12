from django.shortcuts import render
from .models import Food, Consume
# Create your views here.

def index(request):
  user_food = Consume.objects.filter(user=request.user)
  if request.method == 'POST':
    food_consumed = request.POST['food_consumed']
    consume = Food.objects.get(name=food_consumed)
    user = request.user
    consume = Consume(user=user, food_consumed=consume)
    consume.save()
    foods = Food.objects.all()
  else :
    # Get items consumed by currently logged in user
    user_food = Consume.objects.filter(user=request.user)
    foods = Food.objects.all()

  return render(request, 'myapp/index.html', {'foods':foods, 'user_food': user_food})