from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Employee,Projects
from .serializers import EmployeeSerializer,ProjectSerializer
# Create your views here.


class EmployeeView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CrudView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


class ProjectView(ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class ProjectCrudView(RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'