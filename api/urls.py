from django.contrib import admin
from django.urls import path
from .views import EmployeeView,CrudView,ProjectView,ProjectCrudView,ActivityViews,ActivityCrudViews

urlpatterns = [
    path('employee/', EmployeeView.as_view()),
    path('employee/<int:id>', CrudView.as_view()),
    path('projects/', ProjectView.as_view()),
    path('projects/<int:id>/', ProjectCrudView.as_view()),
    path('activity/',ActivityViews.as_view()),
    path('activity/<int:id>', ActivityCrudViews.as_view())

]