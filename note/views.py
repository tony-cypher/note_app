from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import NotesForm
from django.http import HttpResponseRedirect

# Create your views here.

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note/note_list.html'
    login_url = '/login'
 
    def get_queryset(self):
        return self.request.user.my_notes.all()


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'
    # this means from the root url get smart/notes

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'note/note_detail.html'


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/smart/notes'
    template_name = 'note/note_delete.html'