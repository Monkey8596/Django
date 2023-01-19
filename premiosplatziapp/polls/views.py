
from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse('You are in the Home Page Platzi Awards')


def detail(request, question_id):
    return HttpResponse(f'This is the question number {question_id} ')


def results(request, question_id):
    return HttpResponse(f'This is the results of the question number {question_id} ')


def vote(request, question_id):
    return HttpResponse(f'You are voting for the question number {question_id} ')

