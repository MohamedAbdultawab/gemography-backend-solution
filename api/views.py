from django.http import JsonResponse
from .utils import get_repos

# Create your views here.
def list_100_languages(request):
    return JsonResponse(get_repos())