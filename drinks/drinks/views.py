from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

#method to get request
#get all the drink
#serialize them
#retrun json response

def drink_list(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({ 'drinks':serializer.data})


