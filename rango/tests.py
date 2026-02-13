# 
# Tango with Django 2 Progress Tests
# By Leif Azzopardi and David Maxwell
<<<<<<< HEAD
# With assistance from Gerardo A-C (https://github.com/gerac83) and Enzo Roiz (https://github.com/enzoroiz)
# 
# Chapter 10 -- Cookies and Sessions
# Last updated: January 10th, 2020
=======
# With assistance from Enzo Roiz (https://github.com/enzoroiz)
# 
# Chapter 3 -- Django Basics
# Last updated October 3rd, 2019
>>>>>>> ae5c1d0 (3.1)
# Revising Author: David Maxwell
# 

#
# In order to run these tests, copy this module to your tango_with_django_project/rango/ directory.
<<<<<<< HEAD
# Once this is complete, run $ python manage.py test rango.tests_chapter10
=======
# Once this is complete, run $ python manage.py test rango.tests_chapter3
>>>>>>> ae5c1d0 (3.1)
# 
# The tests will then be run, and the output displayed -- do you pass them all?
# 
# Once you are done with the tests, delete the module. You don't need to put it in your Git repository!
#

import os
<<<<<<< HEAD
import re
import rango.models
from rango import forms
from populate_rango import populate
from datetime import datetime, timedelta
from django.db import models
from django.test import TestCase
from django.conf import settings
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.forms import fields as django_fields
=======
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings
>>>>>>> ae5c1d0 (3.1)

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

<<<<<<< HEAD
f"{FAILURE_HEADER} {FAILURE_FOOTER}"


class Chapter10ConfigurationTests(TestCase):
    """
    Tests the configuration of the Django project -- can cookies be used, at least on the server-side?
    """
    def test_middleware_present(self):
        """
        Tests to see if the SessionMiddleware is present in the project configuration.
        """
        self.assertTrue('django.contrib.sessions.middleware.SessionMiddleware' in settings.MIDDLEWARE)
    
    def test_session_app_present(self):
        """
        Tests to see if the sessions app is present.
        """
        self.assertTrue('django.contrib.sessions' in settings.INSTALLED_APPS)


class Chapter10SessionPersistenceTests(TestCase):
    """
    Tests to see if session data is persisted by counting up the number of accesses, and examining last time since access.
    """
    def test_visits_counter(self):
        """
        Tests the visits counter.
        Artificially tweaks the last_visit variable to force a counter increment.
        """
        for i in range(0, 10):
            response = self.client.get(reverse('rango:index'))
            session = self.client.session

            self.assertIsNotNone(session['visits'])
            self.assertIsNotNone(session['last_visit'])

            # Get the last visit, and subtract one day.
            # Forces an increment of the counter.
            last_visit = datetime.now() - timedelta(days=1)

            session['last_visit'] = str(last_visit)
            session.save()

            self.assertEquals(session['visits'], i+1)

class Chapter10ViewTests(TestCase):
    """
    Tests the views manipulated for Chapter 10.
    Specifically, we look for changes to the index and about views.
    """
    def test_index_view(self):
        """
        Checks that the index view doesn't contain any presentational logic for showing the number of visits.
        This should be removed in the final exercise.
        """
        response = self.client.get(reverse('rango:index'))
        content = response.content.decode()

        self.assertTrue('visits:' not in content.lower(), f"{FAILURE_HEADER}The index.html template should not contain any logic for displaying the number of views. Did you complete the exercises?{FAILURE_FOOTER}")
    
    def test_about_view(self):
        """
        Checks to see if the about view has the correct presentation for showing the number of visits.
        """
        response = self.client.get(reverse('rango:index'))  # Call this first to ensure the counter is set.
        response = self.client.get(reverse('rango:about'))
        content = response.content.decode()

        self.assertTrue('Visits: 1' in content, f"{FAILURE_HEADER}In your about.html template, please check that you have the correct output for displaying the number of visits. Capital letters matter. Otherwise, check your about() view and the cookie handling logic.{FAILURE_FOOTER}")
    
    def test_visits_passed_via_context(self):
        """
        Checks that the context dictionary contains the correct values.
        """
        response = self.client.get(reverse('rango:index'))  # Set the counter!
        self.assertNotIn('visits', response.context, f"{FAILURE_HEADER}The 'visits' variable appeared in the context dictionary passed by index(). This should be removed, as per the exercises for Chapter 10.{FAILURE_FOOTER}")

        response = self.client.get(reverse('rango:about'))
        self.assertIn('visits', response.context, f"{FAILURE_HEADER}We couldn't find the 'visits' variable in the context dictionary for about(). Check your about() implementation.{FAILURE_FOOTER}")
=======
class Chapter3ProjectStructureTests(TestCase):
    """
    Simple tests to probe the file structure of your project so far.
    We also include a test to check whether you have added rango to your list of INSTALLED_APPS.
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.rango_app_dir = os.path.join(self.project_base_dir, 'rango')
    
    def test_project_created(self):
        """
        Tests whether the tango_with_django_project configuration directory is present and correct.
        """
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'rango_application'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'rango_application', 'urls.py'))
        
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Your tango_with_django_project configuration directory doesn't seem to exist. Did you use the correct name?{FAILURE_FOOTER}")
        self.assertTrue(urls_module_exists, f"{FAILURE_HEADER}Your project's urls.py module does not exist. Did you use the startproject command?{FAILURE_FOOTER}")
    
    def test_rango_app_created(self):
        """
        Determines whether the Rango app has been created.
        """
        directory_exists = os.path.isdir(self.rango_app_dir)
        is_python_package = os.path.isfile(os.path.join(self.rango_app_dir, '__init__.py'))
        views_module_exists = os.path.isfile(os.path.join(self.rango_app_dir, 'views.py'))
        
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}The rango app directory does not exist. Did you use the startapp command?{FAILURE_FOOTER}")
        self.assertTrue(is_python_package, f"{FAILURE_HEADER}The rango directory is missing files. Did you use the startapp command?{FAILURE_FOOTER}")
        self.assertTrue(views_module_exists, f"{FAILURE_HEADER}The rango directory is missing files. Did you use the startapp command?{FAILURE_FOOTER}")
    
    def test_rango_has_urls_module(self):
        """
        Did you create a separate urls.py module for Rango?
        """
        module_exists = os.path.isfile(os.path.join(self.rango_app_dir, 'urls.py'))
        self.assertTrue(module_exists, f"{FAILURE_HEADER}The rango app's urls.py module is missing. Read over the instructions carefully, and try again. You need TWO urls.py modules.{FAILURE_FOOTER}")
    
    def test_is_rango_app_configured(self):
        """
        Did you add the new Rango app to your INSTALLED_APPS list?
        """
        is_app_configured = 'rango' in settings.INSTALLED_APPS
        
        self.assertTrue(is_app_configured, f"{FAILURE_HEADER}The rango app is missing from your setting's INSTALLED_APPS list.{FAILURE_FOOTER}")
    
class Chapter3IndexPageTests(TestCase):
    """
    Testing the basics of your index view and URL mapping.
    Also runs tests to check the response from the server.
    """
    def setUp(self):
        self.views_module = importlib.import_module('rango.views')
        self.views_module_listing = dir(self.views_module)
        
        self.project_urls_module = importlib.import_module('rango_application.urls')
    
    def test_view_exists(self):
        """
        Does the index() view exist in Rango's views.py module?
        """
        name_exists = 'index' in self.views_module_listing
        is_callable = callable(self.views_module.index)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}The index() view for rango does not exist.{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check that you have created the index() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
    
    def test_mappings_exists(self):
        """
        Are the two required URL mappings present and correct?
        One should be in the project's urls.py, the second in Rango's urls.py.
        We have the 'index' view named twice -- it should resolve to '/rango/'.
        """
        index_mapping_exists = False
        
        # This is overridden. We need to manually check it exists.
        for mapping in self.project_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'index':
                    index_mapping_exists = True
        
        self.assertTrue(index_mapping_exists, f"{FAILURE_HEADER}The index URL mapping could not be found. Check your PROJECT'S urls.py module.{FAILURE_FOOTER}")
        self.assertEquals(reverse('rango:index'), '/rango/', f"{FAILURE_HEADER}The index URL lookup failed. Check Rango's urls.py module. You're missing something in there.{FAILURE_FOOTER}")
    
    def test_response(self):
        """
        Does the response from the server contain the required string?
        """
        response = self.client.get(reverse('rango:index'))
        
        self.assertEqual(response.status_code, 200, f"{FAILURE_HEADER}Requesting the index page failed. Check your URLs and view.{FAILURE_FOOTER}")
        self.assertContains(response, "Rango says hey there partner!", msg_prefix=f"{FAILURE_HEADER}The index view does not return the expected response. Be careful you haven't missed any punctuation, and that your cAsEs are correct.{FAILURE_FOOTER}")
    
    def test_for_about_hyperlink(self):
        """
        Does the response contain the about hyperlink required in the exercise?
        Checks for both single and double quotes in the attribute. Both are acceptable.
        """
        response = self.client.get(reverse('rango:index'))
        
        single_quotes_check = '<a href=\'/rango/about/\'>About</a>' in response.content.decode() or '<a href=\'/rango/about\'>About</a>' in response.content.decode() 
        double_quotes_check = '<a href="/rango/about/">About</a>' in response.content.decode() or '<a href="/rango/about">About</a>' in response.content.decode()
        
        self.assertTrue(single_quotes_check or double_quotes_check, f"{FAILURE_HEADER}We couldn't find the hyperlink to the /rango/about/ URL in your index page. Check that it appears EXACTLY as in the book.{FAILURE_FOOTER}")

class Chapter3AboutPageTests(TestCase):
    """
    Tests to check the about view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """
    def setUp(self):
        self.views_module = importlib.import_module('rango.views')
        self.views_module_listing = dir(self.views_module)
    
    def test_view_exists(self):
        """
        Does the about() view exist in Rango's views.py module?
        """
        name_exists = 'about' in self.views_module_listing
        is_callable = callable(self.views_module.about)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}We couldn't find the view for your about view! It should be called about().{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check you have defined your about() view correctly. We can't execute it.{FAILURE_FOOTER}")
    
    def test_mapping_exists(self):
        """
        Checks whether the about view has the correct URL mapping.
        """
        self.assertEquals(reverse('rango:about'), '/rango/about/', f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")
    
    def test_response(self):
        """
        Checks whether the view returns the required string to the client.
        """
        response = self.client.get(reverse('rango:about'))
        
        self.assertEqual(response.status_code, 200, f"{FAILURE_HEADER}When requesting the about view, the server did not respond correctly. Is everything correct in your URL mappings and the view?{FAILURE_FOOTER}")
        self.assertContains(response, "Rango says here is the about page.", msg_prefix=f"{FAILURE_HEADER}The about view did not respond with the expected message. Check that the message matches EXACTLY with what is requested of you in the book.{FAILURE_FOOTER}")
    
    def test_for_index_hyperlink(self):
        """
        Does the response contain the index hyperlink required in the exercise?
        Checks for both single and double quotes in the attribute. Both are acceptable.
        """
        response = self.client.get(reverse('rango:about'))
        
        single_quotes_check = '<a href=\'/rango/\'>Index</a>' in response.content.decode()
        double_quotes_check = '<a href="/rango/">Index</a>' in response.content.decode()
        
        self.assertTrue(single_quotes_check or double_quotes_check, f"{FAILURE_HEADER}We could not find a hyperlink back to the index page in your about view. Check your about.html template, and try again.{FAILURE_FOOTER}")
>>>>>>> ae5c1d0 (3.1)
