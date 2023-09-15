import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    # 질문
    question_text = models.CharField(max_length=200)
    # 발행일
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # 외래키 - 참조할 테이블 모델: Quesition
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 선택 문구
    choice_text = models.CharField(max_length=200)
    # 투표 집계
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
