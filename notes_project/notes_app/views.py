from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Note, Goal, Tag
from .forms import NoteForm, GoalForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'notes_app/home.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Twoje konto zostało zaktualizowane!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    notes = Note.objects.filter(user=request.user)
    goals = Goal.objects.filter(user=request.user)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'notes': notes,
        'goals': goals,
    }
    
    return render(request, 'notes_app/profile.html', context)

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes_app/note_list.html', {'notes': notes})

@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'notes_app/note_detail.html', {'note': note})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            form.save_m2m()  # To save tags
            return redirect('note_list')
        else:
            print(form.errors)  # Debugging form errors
    else:
        form = NoteForm()
    return render(request, 'notes_app/note_form.html', {'form': form})

@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            form.save_m2m()  # To save tags
            return redirect('note_list')
        else:
            print(form.errors)  # Debugging form errors
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes_app/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')

@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'notes_app/goal_list.html', {'goals': goals})

@login_required
def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    return render(request, 'notes_app/goal_detail.html', {'goal': goal})

@login_required
def goal_create(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            form.save_m2m()  # To save tags
            return redirect('goal_list')
    else:
        form = GoalForm()
    return render(request, 'notes_app/goal_form.html', {'form': form})

@login_required
def goal_edit(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            form.save_m2m()  # To save tags
            return redirect('goal_list')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'notes_app/goal_form.html', {'form': form})

@login_required
def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == "POST":
        goal.delete()
        return redirect('goal_list')
    
@login_required
def goal_complete(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    goal.completed = not goal.completed
    goal.save()
    return redirect('goal_detail', pk=pk)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
