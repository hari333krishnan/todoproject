from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import ListView

from todo_app.models import Todo
from  . forms import Todoform


class TaskListview(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'item'


def home(request):
    if request.method == 'POST':
        task = request.POST['task']
        priority = request.POST['priority']
        time = request.POST['time']
        s = Todo(task=task, priority=priority, time=time)
        s.save()
    odj = Todo.objects.all()
    return render(request, 'home.html', {'item': odj})


def delete(request,id):
    obj = Todo.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    return render(request, 'delete.html', {'product':obj})


def update(request, id):
    objs = Todo.objects.get(id=id)
    '''return render(request, 'style.html', {'ogj':objs})'''
    form = Todoform(request.POST or None, instance=objs)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'obj': objs, 'form': form})
