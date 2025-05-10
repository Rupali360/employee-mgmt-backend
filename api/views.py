from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Employee,Projects,ActivitiesModel
from .serializers import EmployeeSerializer,ProjectSerializer,ActivitySerializer
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


class ActivityViews(ListCreateAPIView):
    queryset = ActivitiesModel.objects.all()
    serializer_class = ActivitySerializer

class ActivityCrudViews(RetrieveUpdateDestroyAPIView):
    queryset = ActivitiesModel.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = 'id'
