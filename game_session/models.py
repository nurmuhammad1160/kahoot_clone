from django.db import models

from game.models import Game, Answer, Question
from users.models import User


# Create your models here.

class GameSession(models.Model):
	game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
	started_at = models.DateTimeField(auto_now_add=True)
	ended_at = models.DateTimeField(blank=True, null=True)
	is_active = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Game Session'
		verbose_name_plural = 'Game Sessions'
		ordering = ['-started_at']

class GameParticipant(models.Model):
	game_session = models.ForeignKey(GameSession, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	answers = models.ManyToManyField(Answer)

	class Meta:
		verbose_name = 'Participant'
		verbose_name_plural = 'Participants'


class ParticipantAnswer(models.Model):
	game_participant = models.ForeignKey(GameParticipant, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	answered_at = models.DateTimeField(auto_now_add=True)
	is_correct = models.BooleanField(default=False)
	time_spent = models.IntegerField(default=0)


	class Meta:
		verbose_name = 'Participant Answer'
		verbose_name_plural = 'Participant Answers'
		ordering = ['time_spent']
