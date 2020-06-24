from django.test import TestCase
from .models import Profile,Project
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime as dt

# Create your tests here.

class ProfileTest(TestCase):
  def setUp(self):
        self.user_ges = User.objects.create_user(username = 'Gesare', password = 'gesare2000')
    
  def test_update_bio(self):
    self.user_ges.profile.update_profile_bio("God is good")
    self.assertEqual(self.user_kim.profile.profile_bio,"God is good")

  def test_search_user_profile(self):
    results =Profile.search_user_profile("Gesare")
    self.assertTrue(len(results)>0)

  def test_get_user_profile(self):
    userprof = Profile.get_user_profile(self.user_ges)
    self.assertEqual(userprof.user.username,self.user_ges.username)

class ProjectTest(TestCase):
  def setUp(self):
    
    self.new_project = Project(title = "KKK",description = "We are a family",live_site = "amazing,org",profile = self.user_kim.profile, pub_date=dt.date.today())
    self.new_project.landing_page = SimpleUploadedFile(name='west.jpg',content=open('/home/martin/Documents/Moringa-Core/Django/awward/media/west.jpg','rb').read(),content_type='image/jpeg')

    self.new_project.save()

  def test_get_single_project(self):
    project = Project.get_single_project(self.new_project.id)
    self.assertEqual(self.new_project.title,"KKK")

  def test_get_all_user_projects(self):
    projects = Project.get_all_projects_user(self.user_kim.profile)
    self.assertTrue(len(projects)==1)

  def test_get_all_projects(self):
    projects = Project.get_all_projects()
    self.assertTrue(len(projects)==1)

  def test_search_project_title(self):
    searched_projects = Project.search_project_title("KKK")
    self.assertTrue(len(searched_projects)==1)

