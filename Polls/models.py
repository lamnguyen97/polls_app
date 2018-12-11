from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("published date")


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    list_filter = ['pub_date']
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length = 200)
    vote = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    def __str__(self):
        return "Choice({}): {} vote".format(self.choice_text, self.vote)
# Create your models here.
