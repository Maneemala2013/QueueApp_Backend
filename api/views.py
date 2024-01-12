from json import JSONDecodeError
from django.http import JsonResponse
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from django.http import Http404
import uuid

class AppointmentList(views.APIView):
    """
    A simple APIView for creating appointment entires.
    """

    model_class = Appointment
    serializer_class = AppointmentSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def get(self, request, format=None):
        snippets = self.model_class.objects.all()
        serializer = self.serializer_class(snippets, many=True)
        print(self.model_class.objects.all())
        return Response(serializer.data)

    def post(self, request):
        try:
            # data = JSONParser().parse(request)
            # serializer = AppointmentSerializer(data=data)
            serializer = AppointmentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
        

class AppointmentDetail(views.APIView):

    model_class = Appointment
    serializer_class = AppointmentSerializer

    def get_object(self, pk):
        try:
            return self.model_class.objects.get(id=pk)
        except self.model_class.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = self.serializer_class(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = self.serializer_class(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
