from django.http import JsonResponse


def index(request):
    return JsonResponse({
        'msg': 'ok',
        'outro campo': 4
    })