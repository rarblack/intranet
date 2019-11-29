from django.test import TestCase
from django.contrib.auth.models import User
from News.models.post.models import PostModel
from News.models.tag.models import TagModel
import random


class RandomPostsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='admin', email='admin@gmail.com', password='admin123')

        tag = TagModel.objects.create(name='test', description='testtest', created_by=user)

        PostModel.objects.create(title='test', body="jsadfjdsakfjsadfjas", created_by=user)
        PostModel.objects.create(title='test', body="jsadfjdsakfjsadfjas", created_by=user)
        PostModel.objects.create(title='test', body="jsadfjdsakfjsadfjas", created_by=user)
        PostModel.objects.create(title='test', body="jsadfjdsakfjsadfjas", created_by=user)
        PostModel.objects.create(title='test', body="jsadfjdsakfjsadfjas", created_by=user)

    @staticmethod
    def get_random_post(length):
        return random.randint(0, length - 1)

    @staticmethod
    def get_length(queryset):
        return len(queryset)

    def test_return_right_amount_of_posts(self):
        posts = PostModel.objects.all()
        posts_length = len(posts)

        if posts_length > 8:
            number = self.get_random_post(posts_length)

            while abs(number - posts_length) < 8:
                number = self.get_random_post(posts_length)

            self.assertEqual(self.get_length(posts[number:number+8]))
