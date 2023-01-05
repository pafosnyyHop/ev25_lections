from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Student
from .serializers import StudentSerializer


class StudentAPIView(APIView):

    def get(self, request):
        students: list[Student] = Student.objects.all()  # ORM requests DJANGO_ORM CLASS.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id=None):
        student = Student.objects.get(pk=id)
        print(student.first_name)
        student.delete()
        return Response('Successfully deleted object')