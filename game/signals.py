from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import QuestionFile, Question

def parse_and_create_questions(question_file_instance):
	file_path = question_file_instance.file.path
	game_id = question_file_instance.game_id

	with open(file_path, 'r', encoding='utf-8') as file:
		for line in file:
			try:
				question_text, question_type, answer_options = line.strip().split(';')
			except ValueError:
				print(f"Skipping invalid line: {line}")
				continue

			Question.objects.create(
				game_id=game_id,
				text=question_text,
				question_type=question_type,
				answer_options=answer_options
			)


@receiver(post_save, sender=QuestionFile)
def process_question_file(sender, instance, created, **kwargs):
	if created and instance.file:
		parse_and_create_questions(instance)
