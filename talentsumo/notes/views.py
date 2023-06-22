from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'profile.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def create_note(request):
    if request.method == 'POST':
        note_type = request.POST['note_type']
        title = request.POST['title']
        content = request.POST['content']
        audio = request.FILES.get('audio')
        video = request.FILES.get('video')
        if note_type == 'text':
            note = Note.objects.create(title=title, content=content, owner=request.user)
        elif note_type == 'audio':
            note = Note.objects.create(title=title, audio=audio, owner=request.user)
        elif note_type == 'video':
            note = Note.objects.create(title=title, video=video, owner=request.user)
        return redirect('view_note', note_id=note.id)
    return render(request, 'create_note.html')


@login_required
def view_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if note.content:
        note_type = 'text'
    elif note.audio:
        note_type = 'audio'
    elif note.video:
        note_type = 'video'
    else:
        note_type = None
    return render(request, 'view_note.html', {'note': note, 'note_type': note_type})


@login_required
def edit_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.audio = request.FILES.get('audio', note.audio)
        note.video = request.FILES.get('video', note.video)
        note.save()
        return redirect('view_note', note_id=note.id)
    return render(request, 'edit_note.html', {'note': note})


@login_required
def share_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get(username=username)
        note.shared_with.add(user)
        return redirect('view_note', note_id=note.id)
    return render(request, 'share_note.html', {'note': note})



@login_required
def view_all_notes(request):
    notes = Note.objects.filter(owner=request.user)
    return render(request, 'view_all_notes.html', {'notes': notes})
