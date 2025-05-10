from rest_framework import serializers
from .models import Employee,Projects,ActivitiesModel
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitiesModel
        fields = '__all__'
        