from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.search import index


class LocationPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [FieldPanel("intro", classname="full")]
    subpage_type = ["SubLocationPage"]


class SubLocationPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [FieldPanel("intro", classname="full")]
    subpage_type = ["JobPage"]


class JobsIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [FieldPanel("intro", classname="full")]
    subpage_types = ["JobPage"]


class JobPage(Page):
    locationcode = models.CharField(max_length=20)
    locationname = models.CharField(max_length=250)
    jobcode = models.CharField(max_length=10, blank=True)
    datedue = models.DateField("Next due date")
    datedone = models.DateField("Last done date")
    jobtitle = models.CharField(max_length=60, blank=True)
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    subsystem = models.CharField(max_length=120, blank=True)
    vessel_comment = RichTextField(blank=True)
    responsible_crew = models.CharField(max_length=30, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("locationname"),
        FieldPanel("locationcode"),
        FieldPanel("datedone"),
        FieldPanel("datedue"),
        FieldPanel("intro"),
        FieldPanel("body", classname="full"),
    ]

    subpage_types = ["JobCardPage"]


class JobCardPage(Page):
    datedone = models.DateField("Last done date")
    datedue = models.DateField("Next due date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("datedone"),
        FieldPanel("datedue"),
        FieldPanel("intro"),
        FieldPanel("body", classname="full"),
    ]
