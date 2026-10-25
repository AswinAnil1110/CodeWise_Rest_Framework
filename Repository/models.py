from django.db import models

"""
Schema Name : QuestionDb
Fields      : title, language, difficutly_level, score, topic, notes,
              published_date, sample_input, sample_output, is_active
"""
# Create your models here.

class QuestionDb(models.Model):
    title = models.CharField(max_length=200)
    language_choice = (
                        ('python','Python'),
                        ('java','Java'),
                        ('cpp','C++')
                      )
    language = models.CharField(max_length=100,choices=language_choice)
    diificutly_choice = (
                          ('easy','Easy'),
                          ('medium','Medium'),
                          ('hard','Hard')
                        )
    difficutly_level = models.CharField(max_length=100,choices=diificutly_choice)
    score = models.IntegerField()
    topic = models.CharField(max_length=200)
    notes = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    sample_input = models.TextField()
    sample_output = models.TextField()
    is_active = models.BooleanField(default=True)
  
class SubmissionDb(models.Model):
  answer = models.TextField()
  question_id = models.IntegerField()
  owner = models.CharField(max_length=100)
  points = models.PositiveIntegerField(null=True)
  submission_date = models.DateTimeField(auto_now_add=True)
  remarks = models.TextField()