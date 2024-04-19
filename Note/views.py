from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note

class NoteList(ListView):
    model = Note
    template_name = 'note_list.html'

from django.views.generic.edit import CreateView
from .models import Note
from .forms import NoteForm
from django.urls import reverse_lazy

class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm  # Utilisation du formulaire personnalisé
    template_name = 'note_form.html'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Si vous avez un champ 'author' dans votre modèle Note
        return super().form_valid(form)


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
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('note_list')