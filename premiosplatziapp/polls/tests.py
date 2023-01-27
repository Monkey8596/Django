import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Models
# Views
class QuestionModelTests(TestCase):

    def  test_was_published_recently_with_future_questions(self):
        
        '''
        was_published_recently returns False for the questions whose pub_date is inn the future
        '''

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question( question_text='Whos is the best Course Director on Platzi' , pub_date = time )
        self.assertIs(future_question.was_published_recently(), False)