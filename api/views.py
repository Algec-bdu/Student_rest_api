from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students
from .serializers import StudentsSerializer

# Create your views here.


@api_view(['GET'])
def studentView(request):
    students = Students.objects.all()
    serializer = StudentsSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createStudent(request):
    serializer = StudentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data
