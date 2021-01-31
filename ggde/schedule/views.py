from django.http import JsonResponse
from ggde.utils import create_schedule
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny


class ScheduleView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    @api_view(['POST'])
    def mount_schedule(request):
        print(request.data)

        if request.method == 'POST':
            return JsonResponse(
                create_schedule(request.data["subjects"], request.data["availabilities"])
            )
        
        return JsonResponse({'KEY': 'OK'})