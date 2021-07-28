from django.test import TestCase
from .models import *

# Create your tests here.
class TestProfile(TestCase):
  def setUp(self):
    self.user = User(id=1, username='salome', password='salome8888')
    self.user.save()

  def test_instance(self):
    self.assertTrue(isinstance(self.user, User))

  def test_save_user(self):
    self.user.save()

  def test_delete_user(self):
    self.user.delete()
    
class BusinessTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='salome')
    self.neighborhood = Neighborhood.objects.create(id=1, name='neighborhood')
    self.business = Business.objects.create(id=1, name='business',pub_date='2021,07,27',address='random_number')

  def test_instance(self):
    self.assertTrue(isinstance(self.busines, Business))

  def test_create_business(self):
    self.busines.create_business()
    business = Business.objects.all()
    self.assertTrue(len(business) > 0)

  def test_get_business(self, id):
    self.business.save()
    business = Business.get_businesss(post_id=id)
    self.assertTrue(len(business) == 1)        

class PostTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='salome')
    self.neighborhood = Neighborhood.objects.create(id=1, name='neighborhood')
    self.posts = Posts.objects.create(id=1,pub_date='2021.07,27',author_profile='image')

  def test_instance(self):
    self.assertTrue(isinstance(self.posts, Posts))

  def test_display_posts(self):
    self.posts.save()
    posts = Posts.all_posts()
    self.assertTrue(len(posts) > 0)

  def test_save_post(self):
    self.posts.save_posts()
    posts = Posts.objects.all()
    self.assertTrue(len(posts) > 0)

  def test_delete_post(self):
    self.posts.delete_posts()
    posts = Posts.search_posts('random_post')
    self.assertTrue(len(posts) < 1)

class NeighborhoodTest(TestCase):
  def setUp(self):
    self.user = User.objects.create(id=1, username='salome')
    self.neighborhood = Neighborhood.objects.create(id=1, name='business',location='neighborhood',admin='salome',occupants_count=1)

  def test_create_neighborhood(self):
    self.neighborhood.create_neighborhood()
    neighborhood = Neighborhood.objects.all()
    self.assertTrue(len(neighborhood) > 0)

  def test_get_neighborhood(self, id):
    self.neighborhood.save()
    neighborhood = Neighborhood.get_neighborhood(neighborhood_id=id)
    self.assertTrue(len(neighborhood) == 1)    
