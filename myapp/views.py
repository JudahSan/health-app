from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.

def index(request):
  if request.method == 'POST':
    food_consumed = request.POST['food_consumed']
    consume = Food.objects.get(name=food_consumed)
    user = request.user
    consume = Consume(user=user, food_consumed=consume)
    consume.save()
    foods = Food.objects.all()
  else :
    # Get items consumed by currently logged in user
    foods = Food.objects.all()
  user_food = Consume.objects.filter(user=request.user)
  return render(request, 'myapp/index.html', {'foods':foods, 'user_food': user_food})

def del_food(request, id):
  food_item = Consume.objects.get(id=id)
  if request.method == 'POST':
    food_item.delete()
    return redirect('/')
  return render(request, 'myapp/delete.html')