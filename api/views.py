from django.http import JsonResponse
from rest_framework.views import APIView

# Create your views here.
class SampleView(APIView):
    def get(self, request):
        return JsonResponse({'data': 'Hello World!'})