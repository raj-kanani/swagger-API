from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView


class SwaggerAPI(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def get(self, request):
    #     objects = Student.objects.all()
    #     serializer = StudentSerializer(objects, many=True)

    # def post(self, request):
    #     data = request.data
    #     obj = Student.objects.create(firstname=data['firstname'], lastname=data['lastname'])
    #     return HttpResponse('student is created....')
