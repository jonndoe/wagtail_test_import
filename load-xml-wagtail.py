import json
import os
from pathlib import Path

"""
from django.conf import settings as settings
from django.contrib.contenttypes.models import ContentType
from django.core.files import File
from django.core.management.base import BaseCommand
from wagtail.core.models import Page, Site
from wagtail.images.models import Image
from mainproject.mainproject.settings import dev as settings
"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainproject.mainproject.settings.dev")

from mainproject.jobs.models import JobPage, JobsIndexPage

APP_DIR = Path(__file__).resolve().parent
FIXTURES_DIR = APP_DIR.joinpath("fixtures")


jobsindexpage = JobsIndexPage.objects.get()


print("jobindexpage", jobsindexpage)
