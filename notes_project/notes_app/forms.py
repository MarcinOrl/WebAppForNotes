from django.contrib.auth.models import User
from django import forms
from .models import Note, Goal, Profile, Tag
from django_select2.forms import Select2TagWidget

class NoteForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=Select2TagWidget
    )
    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'froala-editor'}),
        }

class GoalForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=Select2TagWidget
    )
    class Meta:
        model = Goal
        fields = ['title', 'description', 'due_date', 'completed', 'tags']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']