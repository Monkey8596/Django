import datetime

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

from .models import Question

# Models
# Views
class QuestionModelTests(TestCase):

    def  test_was_published_recently_with_future_questions(self):
        
        '''
        
        was_published_recently returns False for the questions whose pub_date is in the future
        
        '''

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question( question_text='Whos is the best Course Director on Platzi' , pub_date = time )
        self.assertIs(future_question.was_published_recently(), False)


    def  test_was_published_recently_with_past_questions(self):
        
        '''
        
        was_published_recently returns False for the questions whose pub_date is in the past
        
        '''

        time = timezone.now() - datetime.timedelta(days=30)
        past_question = Question( question_text='Whos is the best Course Director on Platzi' , pub_date = time )
        self.assertIs(past_question.was_published_recently(), False)


    def  test_was_published_recently_with_questions(self):
        
        '''
        
        was_published_recently returns True for the questions whose pub_date is recently
        
        '''

        time = timezone.now()
        recent_question = Question( question_text='Whos is the best Course Director on Platzi' , pub_date = time )
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        '''
        
        If no question exist, an appropiate message is displpayed
        
        '''

        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def  test_no_future_questions(self):
        
        '''
        
        Question created in the future is not included in latest_question_list
        
        '''

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question( question_text='Whos is the best Course Director on Platzi' , pub_date = time )
        #future_question.save()
        response = self.client.get(reverse('polls:index'))
        self.assertNotIn(future_question, response.context['latest_question_list'])

    
