from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import CreatedataForm, TodoUpdateForm


# Create your views here.
def hello(request):
    all_of_objects = Todo.objects.all()
    return render(request, 'home.html', {'all': all_of_objects})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'Deleting has been successfully...', 'success')
    return redirect('home')


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'your todo updated... ')
            return redirect('details', todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
        return render(request, 'update.html', {'form': form})


def create(request):
    if request.method == 'POST':
        form = CreatedataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Todo.objects.create(title=data['title'], body=data['body'], date_created=data['date_created'])
            messages.success(request, 'Articles created successfully....', 'success')
            return redirect('home')
    else:
        form = CreatedataForm()
        return render(request, 'create.html', {'form': form})
