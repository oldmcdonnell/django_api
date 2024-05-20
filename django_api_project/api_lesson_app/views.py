from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
#veiws are vanillia, vewsets are django-rest to handle the endpoint

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all() #can be filtered down
    serializer_class = StudentSerializer


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def create(self, request):
        mutable_data_copy = request.data.copy()
        mutable_data_copy['name'] = f'Professor {mutable_data_copy['name']}'

        serializer = InstructorSerializer(data = mutable_data_copy)
        serializer.is_valid(raise_exception=True)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

def get_letter_grade(obj):
    if (obj.score >= 90):
        return 'A'
    elif(obj.score >= 80):
        return 'B'
    elif(obj.score >= 70):
        return 'C'
    elif(obj.score >= 60):
        return 'D'
    else:
        return 'F'

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def retrieve(self, request, pk=None):
        grade = Grade.objects.get(pk=pk)
        grade_serializer = GradeSerializer(grade)
        data = grade_serializer.data
        data['letter_grade'] = get_letter_grade(grade)
        return Response(data)
