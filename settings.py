# TODO: Slowly get rid of this file.
from dotenv import load_dotenv
load_dotenv()
import os

#In here all settings, all variables can be configured here.
slackLA = "#losangeles"
slackNY = "#newyork"
slackToken = os.getenv("SLACK_TOKEN")

#Indeed Api:-----------------------------------------------------------------------------------------------------
useIndeed = True
indeedToken = os.getenv("INDEED_TOKEN")
JobKeywords = ["Python Internship","Web Developer Internship","python intern","web developer intern","Computer Science Internship"]
cities = ['Los Angeles']
# Cities: cities = ['Los Angeles', 'New York']

#Craigslist Api:-------------------------------------------------------------------------------------------------
useCraigslist = True
jobCategorys = ['sof', 'jjj']
want_internship = True
resultNumber = 3 #Be careful with this, don't bring back too many results.
Craigslistcities = ['losangeles']
# Craigslistcities = ['losangeles','newyork']

areas = {'losangeles': ['lac']}
# areas = {'losangeles': ['lac'] , 'newyork': ['mnh','brk','que','brx']}
