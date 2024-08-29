from django.db import models

"""
Create your models here.
This Python class defines a model for a question with text and
publication date fields.
"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published0')

    def __str__(self):
        return self.question_text


"""
The `Choice` class represents a choice option for a question with attributes for choice text and
number of votes.
"""


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
