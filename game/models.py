from django.db import models

from users.models import User


# Create your models here.
class Game(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField()
	is_visible = models.BooleanField(default=True)
	image = models.ImageField(upload_to='games/', blank=True, null=True)
	language = models.CharField(max_length=100, default='en', blank=True, null=True)
	is_active = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
	QUESTION_TYPES = (
		('quiz', 'Quiz'),
		('true_false', 'True or False'),
		('slider', 'Slider'),
		('type_answer', 'Type answer'),
		('pin_answer', 'Pin answer'),
		('Puzzle', 'Puzzle'),
	)
	ANSWER_OPTIONS = (
		('single_select', 'Single select'),
		('multiple_select', 'Multiple select'),
	)
	game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
	text = models.TextField()
	question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='quiz')
	answer_options = models.CharField(max_length=20, choices=ANSWER_OPTIONS, default='single_select')
	image = models.ImageField(upload_to='questions/', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Question'
		verbose_name_plural = 'Questions'
		ordering = ['-created_at']


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.TextField()
	is_correct = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Answer'
		verbose_name_plural = 'Answers'
		ordering = ['-created_at']








