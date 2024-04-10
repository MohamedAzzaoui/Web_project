from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note

class NoteList(ListView):
    model = Note
    template_name = 'note_list.html'

class NoteCreate(CreateView):
    model = Note
    template_name = 'note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('note_list')

class NoteDetail(DetailView):
    model = Note
    template_name = 'note_detail.html'

class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'note_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('note_list')

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('note_list')