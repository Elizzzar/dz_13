from django.urls import path
from app.views import *
from django.urls import re_path

# Домашка 13:  1. Используя знания регулярных выражений, подготовьте маршруты к проекту типа «Лист задач».
# 2. Дайте каждому маршруту уникальное имя и примерно в комментарии опишите его функционал.

urlpatterns = [
    # Главная страница и отображает список всех задач.
    path('', TaskListView.as_view(), name='task_list'),
    # Страница добавление новых задач.
    path('create/', TaskCreateView.as_view(), name='task_create'),
    # Страница подробного просмотра. Принимает иденификатор задачи в качестве параметра.
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    # Страница обновления задачи чтобы поменять значения.
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    # Страница удаления задачи и тоже принимает идентификатор
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]

# urlpatterns = [
#     re_path(r'^$', TaskListView.as_view(), name='task_list'),
#     re_path(r'^create$', TaskCreateView.as_view(), name='task_create'),
#     re_path(r'^(?P<pk>\d+)/$' ,TaskDetailView.as_view(), name='task_detail'),
#     re_path(r'^(?P<pk>\d+)/update$' ,TaskUpdateView.as_view(), name='task_update'),
#     re_path(r'^(?P<pk>\d+)/delete$' ,TaskDeleteView.as_view(), name='task_delete'),
# ]
