from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Answer
from .forms import AnswerForm


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()
    current_question = questions.first()  

    feedback = None 

    if request.method == 'POST':
        form = AnswerForm(request.POST, question=current_question)
        if form.is_valid():
            user_answer = form.cleaned_data['answer']
            if user_answer.is_correct:
                feedback = "To‘g‘ri!"
            else:
                feedback = "Noto‘g‘ri."
    else:
        form = AnswerForm(question=current_question)

    return render(request, 'quiz_detail.html', {
        'quiz': quiz,
        'question': current_question,
        'form': form,
        'feedback': feedback
    })


def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quiz_result.html', {'quiz': quiz})
