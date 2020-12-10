from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from students.forms import StudentsForm
from students.models import Students
from .serializers import StudentsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def std(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = StudentsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list_view")
    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Students.objects.all()

    return render(request, "list_view.html", context)


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Students.objects.get(id=id)

    return render(request, "detail_view.html", context)


# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Students, id=id)

    # pass the object as instance in form
    form = StudentsForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list_view")

        # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Students, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/list_view")

    return render(request, "delete_view.html", context)


@api_view(['GET'])
def studentsList(request):
    std1 = Students.objects.all()
    serializer = StudentsSerializer(std1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def studentsDetail(request, pk):
    std1 = Students.objects.get(id=pk)
    serializer = StudentsSerializer(std1, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def studentsAdd(request):
    serializer = StudentsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def studentsUpdate(request, pk):
    std1 = Students.objects.get(id=pk)
    serializer = StudentsSerializer(instance=std1, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def studentsDelete(request, pk):
    std1 = Students.objects.get(id=pk)
    std1.delete()

    return Response('Item Successfully Delete!')
