from django.shortcuts import render
from employee.models import Employee


def emp_view(request):
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Employee.objects.raw('SELECT id, emp_name, emp_age FROM employee')

    return render(request, "emp_list.html", context)
