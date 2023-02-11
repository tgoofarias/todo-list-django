from django.shortcuts import render,redirect
import requests


def index(request):
    if request.method == 'GET':
        response = requests.get('http://localhost:8000/api/tasks/').json()
        return render(request, 'todo/index.html', {'tasks': response})
    if request.method == 'POST':
        title = request.POST['title']
        json = {'title': title}
        response = requests.post('http://localhost:8000/api/tasks/', json)
        return redirect('index')


def delete_task(request, pk):
    url = f'http://localhost:8000/api/tasks/{pk}/'
    requests.delete(url)
    return redirect('index')


def update_task(request, pk):
    if request.method == 'GET':
        url = f'http://localhost:8000/api/tasks/{pk}/'
        response = requests.get(url).json()
        json = {'id': response['id'] ,'title': response['title'], 'is_completed': response['is_completed']}
        return render(request, 'todo/update-task.html', {'task': json})

    elif request.method == 'POST':
        url = f'http://localhost:8000/api/tasks/{pk}/'
        new_title = request.POST['new_title']
        is_completed = request.POST.get('is_completed', False)
        if is_completed == 'on':
            is_completed = True
        json = {'title': new_title, 'is_completed': is_completed}
        response = requests.put(url, json)
        return redirect('index')
