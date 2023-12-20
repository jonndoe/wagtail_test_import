import random
import time
import xml.etree.ElementTree as ET
from xml.dom.minidom import Node, parse

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from jobs.models import JobPage, JobsIndexPage, LocationPage, SubLocationPage


class Command(BaseCommand):
    def handle(self, *args, **options):
        tree = ET.parse("all_jobs.XML")
        root = tree.getroot()

        print("hello")
        job_index_page = JobsIndexPage.objects.all().first()
        print(job_index_page)

        """Creates the job pages."""
        parent_page = job_index_page

        jobpage_content_type = ContentType.objects.get_for_model(JobPage)
        # For each job in xml file, create a new jobpage
        # for language_code, label in settings.LANGUAGES:
        for i in range(0, 1):
            if True is True:
                locationname = "this is location name"
                locationcode = "this is locat code"
                datedone = time.strftime("%Y-%m-%d", time.localtime())
                datedue = time.strftime("%Y-%m-%d", time.localtime())
                intro = "this is intro"
                body = "this is body of the text"
                title = "this is title" + str(random.randint(0, 1000))
                slug = slugify(title)

            else:
                raise RuntimeError(f"some problem happened......")
            jobpage = JobPage(
                locationname=locationname,
                locationcode=locationcode,
                datedone=datedone,
                datedue=datedue,
                intro=intro,
                body=body,
                title=title,
                # slug=slugify(title)
                slug=slug,
                content_type=jobpage_content_type,
            )
            parent_page.add_child(instance=jobpage)
            print("jobpage added!!!!")

            counter = 0
            for i in root[0]:
                print(i.tag)  # All_jobs_long_v7_group1
                for j in i:
                    print("    ", j.tag)  # location_code  AND   All_jobs_long_v7_group2
                    if j.tag != "location_code":
                        for k in j:  # All_jobs_long_v7_group2
                            print("    ", k.tag)  # All_jobs_long_v7_group3
                            for v in k:
                                print("        ", v.tag)  # All_jobs_long_v7_group4
                                # print(v)
                                for r in v:  # For each job in xml file
                                    print(
                                        "            ", r.tag
                                    )  # All_jobs_long_v7_group5

                                    if r.tag != "jobs_library_crew":
                                        print(
                                            "+++++++++++++",
                                            r.tag,
                                            "entered job:",
                                            counter,
                                        )
                                        counter += 1
                                        # print(g.text)
                                        # print(g.attrib)
                                        print(
                                            "_________________started creating the job:"
                                        )

                                        if True is True:
                                            locationname = r[12].text
                                            locationcode = r[13].text
                                            datedone = time.strftime(
                                                "%Y-%m-%d", time.localtime()
                                            )
                                            datedue = time.strftime(
                                                "%Y-%m-%d", time.localtime()
                                            )
                                            intro = r[11].text
                                            body = r[28].text
                                            title = (
                                                r[2].text
                                                + "-"
                                                + str(random.randint(0, 1000))
                                                + str(random.randint(0, 20000))
                                            )
                                            slug = slugify(title)

                                        else:
                                            raise RuntimeError(
                                                f"some problem happened......"
                                            )
                                        jobpage = JobPage(
                                            locationname=locationname,
                                            locationcode=locationcode,
                                            datedone=datedone,
                                            datedue=datedue,
                                            intro=intro,
                                            body=body,
                                            title=title,
                                            slug=slug,
                                            content_type=jobpage_content_type,
                                        )
                                        parent_page.add_child(instance=jobpage)
                                        print("jobpage added!!!!")

                                        for field in r:  # For each field in job
                                            # if field.text is not None:
                                            # print('++++++++Entered jobs of type:', f.text)
                                            print(
                                                "                                ",
                                                field.tag,
                                                field.text,
                                            )
                                            # print(field.attrib)

        def print_nodes_2(parent):
            counter = 0
            for i in parent:
                print(i.tag)  # All_jobs_long_v7_group1
                for j in i:
                    print("    ", j.tag)  # location_code  AND   All_jobs_long_v7_group2
                    if j.tag != "location_code":
                        for k in j:  # All_jobs_long_v7_group2
                            print("    ", k.tag)  # All_jobs_long_v7_group3
                            for v in k:
                                print("        ", v.tag)  # All_jobs_long_v7_group4
                                # print(v)
                                for r in v:  # For each job in xml file
                                    print(
                                        "            ", r.tag
                                    )  # All_jobs_long_v7_group5

                                    if r.tag != "jobs_library_crew":
                                        print(
                                            "+++++++++++++",
                                            r.tag,
                                            "entered job:",
                                            counter,
                                        )
                                        counter += 1
                                        # print(g.text)
                                        # print(g.attrib)

                                        for field in r:  # For each field in job
                                            if field.text is not None:
                                                # print('++++++++Entered jobs of type:', f.text)
                                                print(
                                                    "                                ",
                                                    field.text,
                                                )

        tree = ET.parse("all_jobs.XML")
        root = tree.getroot()
        print_nodes_2(root[0])
