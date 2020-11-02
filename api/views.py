from django.http import JsonResponse
from django.http.response import HttpResponseNotFound, HttpResponseServerError
from .utils import get_languages

# Create your views here.
def list_trending_languages(request):
    """API endpoint to list the languages used by the 100 trending public repos on GitHub.

    Args:
        request (WSGIRequest): django incoming request

    Returns:
        JsonResponse:           Languages used by the 100 trending public repos on GitHub.
        [HttpResponseNotFound]: [if request is not GET]
    """
    if not request.method == "GET":
        return HttpResponseNotFound()

    try:
        data = get_languages()
        return JsonResponse(data)
    except:
        return HttpResponseServerError