from django.shortcuts import redirect, render
from polls.models import Student
from django.http import HttpResponse
# Create your views here.




def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        fm = Student(name=name, email=email, phone=phone)
        fm.save()
        return redirect('index')
    else:
        fm = Student.objects.all()
        return render(request, 'polls/index.html', {'fm':fm})
    # return HttpResponse("Hello, world. You're at the polls index.")

def edit(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        fm = Student(id=id, name=name, email=email, phone=phone)
        fm.save()
        return redirect('index')
    else:
        fm = Student.objects.get(id=id)
        return render(request, 'polls/edit.html', {'fm':fm})

def delete(request, id):
    fm = Student.objects.get(id=id)
    fm.delete()
    return redirect('index')
