import os

from django.test import Client, TestCase

from en.models import MuseumModel as EnMuseumModel
from en.models import PostModel as EnPostModel
from en.models import TopicModel as EnTopicModel
from ptbr.models import MuseumModel as PtMuseumModel
from ptbr.models import PostModel as PtPostModel
from ptbr.models import TopicModel as PtTopicModel


class Test(TestCase):
    def setUp(self):
        topic = EnTopicModel.objects.create(name='Test')
        EnPostModel.objects.create(topic=topic, title='Test', body='Test', image=('tests/Eduardo_Kac_and_Alba_the_fluorescent_bunny_photo_by_Chrystelle_Fontaine.jpeg'))
        EnMuseumModel.objects.create(title='Test', image=('tests/Eduardo_Kac_and_Alba_the_fluorescent_bunny_photo_by_Chrystelle_Fontaine.jpeg'))

    def test_(self):
        c = Client(enforce_csrf_checks=True)
        c.get('/')

        c.get('/en/')
        c.get('/en/blog/')

        c.get('/pt-br/')
        c.get('/pt-br/blog/')
