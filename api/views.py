from django.http import JsonResponse
from .utils import get_languages

# Create your views here.
def list_100_languages(request):
    return JsonResponse(get_languages())