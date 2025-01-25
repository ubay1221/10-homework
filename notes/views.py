from django.shortcuts import render, redirect,get_object_or_404
from .models import Note


def home(request):
    return render(request,'index.html')

def note_list(request):
    notes = Note.objects.all()
    ctx = {'notes':notes}
    return render(request, 'notes/note-list.html', ctx)

def create_note(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        if title and content:
            Note.objects.create(
                title = title,
                content = content
            )
            return redirect('notes:list')
    return render(request, 'notes/notes-create.html')

def note_detail(request, notes_id):
    notes = get_object_or_404(Note, pk=notes_id)
    ctx = {'notes':notes}
    return render(request, 'notes/notes-detail.html', ctx)

def note_update(request, notes_id):
    notes = get_object_or_404(Note, pk=notes_id)
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        if title and content:
            notes.title = title
            notes.content = content
            notes.save()
            return redirect(notes.get_detail_url())
    ctx = {'notes':notes}
    return render(request, 'notes/notes-create.html', ctx)

def note_delete(request, notes_id):
    notes = get_object_or_404(Note, pk=notes_id)
    notes.delete()
    return redirect('notes:list')