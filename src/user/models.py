import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
class Evento(models.Model):
    nome = models.CharField(max_length=200)
    horario = models.DateTimeField("Data e Horário do Evento")
    local = models.CharField(max_length=250)
    descricao = models.TextField("Breve Descrição", blank=True, null=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"    