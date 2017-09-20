# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from quiz_round_app.models import Question, Answer

class QuestionTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password='neosoft@123')
        question = Question.objects.create(title="what is json?", is_private=False , user=user)
        answer = Answer.objects.create(body="Java script object", question=question, user=user)

    def test_user_present_for_question(self):
        """Test availability of user who raise question"""
        question = Question.objects.get(title="what is json?")
        self.assertIsNotNone(question.user, msg="User available")


class AnswerTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password='neosoft@123')
        question = Question.objects.create(title="what is json?", is_private=False , user=user)
        answer = Answer.objects.create(body="Java script object", question=question, user=user)

    def test_answer_having_right_question(self):
        """Test answering for correct question or not"""
        question = Question.objects.get(title="what is json?")
        answers = Answer.objects.filter(question=question)
        for answer in answers:
            self.assertIsNotNone(answer.question, msg="question available")
            self.assertEquals(answer.question.title, question.title)

    def test_user_present_for_answer(self):
        """Test availability of user who answered question"""
        question = Question.objects.get(title="what is json?")
        answers = Answer.objects.filter(question=question)
        for answer in answers:
            self.assertIsNotNone(answer.user, msg="User available")