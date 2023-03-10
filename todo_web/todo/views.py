from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

from .models import AddTask


def reset_func(request):
    for _ in range(1, 21):
        check_status = False
        task = ''
        date = '2023-02-23'
        time = '00:00'

        new_task = AddTask(task_id=_, check_status=check_status, task=task, date=date, time=time)
        new_task.save()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")


def home(request):
    if request.method == 'POST':
        list_task = [task for num, task in enumerate(request.POST) if num > 0]
        task_dic = {task_name: request.POST[task_name] for task_name in list_task}

        for _ in range(1, 21):
            try:
                a = task_dic[f'check_status_{_}']
                check_status = True
            except KeyError:
                check_status = False
            task = task_dic[f'task_{_}']
            if task_dic[f'date_{_}'] != '':
                date = task_dic[f'date_{_}']
            else:
                date = timezone.now()
            if task_dic[f'time_{_}'] != '':
                time = task_dic[f'time_{_}']
            else:
                time = timezone.now()

            new_task = AddTask(task_id=_, check_status=check_status, task=task, date=date, time=time)
            new_task.save()
    tasks_data = AddTask.objects.all()
    return render(request, 'todo/index.html', {'myrange': range(1, 21), 'tasks_data': tasks_data})
