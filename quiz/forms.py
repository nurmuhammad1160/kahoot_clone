from django import forms
from .models import Answer, Question

class AnswerForm(forms.Form):
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answer_set.all()

