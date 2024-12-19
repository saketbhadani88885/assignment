from django.http import HttpResponse
# from rest_framework.response import Response
from rest_framework.views import APIView
from task.task import print_msg

class CreateTask(APIView):
    def get(self, request):
        print_msg.apply_async(countdown=3)
        return HttpResponse({"Created a task"})
