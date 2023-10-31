from . import views
from django.urls import path, include

urlpatterns = [
    path('notes/', views.NoteListView.as_view(), name='note.list'),
    path('notes/new', views.NoteCreateView.as_view(), name='note.create'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name='note.detail'),
    path('notes/<int:pk>/edit', views.NoteUpdateView.as_view(), name='note.update'),
    path('notes/<int:pk>/delete', views.NoteDeleteView.as_view(), name='note.delete'),
]