from django.urls import path
from .views import (
    note_list, note_detail, note_create, note_edit, note_delete,
    goal_list, goal_detail, goal_create, goal_edit, goal_delete,
    home  # Dodaj import widoku głównego
)

urlpatterns = [
    path('', home, name='home'),  # Dodaj ścieżkę dla widoku głównego
    path('notes/', note_list, name='note_list'),
    path('notes/<int:pk>/', note_detail, name='note_detail'),
    path('notes/new/', note_create, name='note_create'),
    path('notes/<int:pk>/edit/', note_edit, name='note_edit'),
    path('notes/<int:pk>/delete/', note_delete, name='note_delete'),
    path('goals/', goal_list, name='goal_list'),
    path('goals/<int:pk>/', goal_detail, name='goal_detail'),
    path('goals/new/', goal_create, name='goal_create'),
    path('goals/<int:pk>/edit/', goal_edit, name='goal_edit'),
    path('goals/<int:pk>/delete/', goal_delete, name='goal_delete'),
]