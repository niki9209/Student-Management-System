from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentsModel


# Create your views here.
def home(request):
    return render(request, 'home.html')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('mail')
        degree = request.POST.get('degree')
        course = request.POST.get('course')

        StudentsModel.objects.create(
            name=name,
            contact=contact,
            email=email,
            degree=degree,
            course=course
        )

        return redirect('display')

    return render(request, 'create.html')


def about(request):
    return render(request, 'about.html')


def display(request):
    data = StudentsModel.objects.all()
    return render(request, 'display.html', {'data': data})


def update(request, uid):
    user = get_object_or_404(StudentsModel, id=uid)

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.contact = request.POST.get('contact')
        user.email = request.POST.get('mail')
        user.degree = request.POST.get('degree')
        user.course = request.POST.get('course')

        user.save()

        return redirect('display')

    return render(request, 'update.html', {'user': user})


def delete(request, uid):
    user = get_object_or_404(StudentsModel, id=uid)

    if request.method == 'POST':
        user.delete()

        return redirect('display')

    return render(request, 'delete.html', {'user': user})


def help(request):
    return render(request, 'help.html')