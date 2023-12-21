import random
import time
import xml.etree.ElementTree as ET
from xml.dom.minidom import Node, parse

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from jobs.models import JobPage, JobsIndexPage, LocationPage, SubLocationPage
from wagtail.core.models import Page, Site


class Command(BaseCommand):
    def handle(self, *args, **options):
        tree = ET.parse("all_jobs.XML")
        root = tree.getroot()

        """Creates the ship_page page"""
        wagtail_root = Page.get_first_root_node()
        jobsindexpage_content_type = ContentType.objects.get_for_model(JobsIndexPage)
        intro = "this is intro for ShipPage"
        slug = slugify(intro)
        job_index_page = JobsIndexPage(
            title="GAS COBIA",
            intro=intro,
            slug=slug,
            content_type=jobsindexpage_content_type,
        )
        wagtail_root.add_child(instance=job_index_page)

        """
        # Create a site with a new job_index_page set as the root
        Site.objects.create(
            hostname="localhost",
            root_page=job_index_page,
            is_default_site=True,
            site_name="tecshippms.com",
        )
        """

        # create location pages which are the child of ship_page
        ship_page = JobsIndexPage.objects.all().first()

        """Creates the job pages."""
        parent_page = job_index_page
        jobpage_content_type = ContentType.objects.get_for_model(JobPage)

        locations = []
        jobs_library_crew_list = []

        def create_jobs_list_frame(parent):
            total_jobs_counter = 0
            locations_counter = 0
            location_name_var = "noname"

            for group1 in parent:
                for (
                    group2
                ) in group1:  # location_code  AND   All_jobs_long_v7_group2 in group1
                    if group2.tag == "location_code":
                        location_code = []
                        location_code.append(group2.text)
                        location_code_text = group2.text
                        locations.append(location_code)

                        # create location page
                        location_name_var = group2.text
                        ship_page = JobsIndexPage.objects.all().first()
                        jobsindexpage_content_type = ContentType.objects.get_for_model(
                            JobsIndexPage
                        )
                        title = group2.text
                        intro = "this is intro for " + title
                        slug = slugify(intro)
                        location_page = JobsIndexPage(
                            title=group2.text,
                            intro=intro,
                            slug=slug,
                            content_type=jobsindexpage_content_type,
                        )
                        ship_page.add_child(instance=location_page)

                        # create corresponding sublocation_page here for each location
                    else:  # group2.tag != "location_code":
                        for (
                            group3
                        ) in group2:  # job_type and All_jobs_long_v7_group3 in group2
                            if group3.tag == "job_type":
                                job_type = []
                                job_type.append(group3.text)
                                pass
                            else:
                                for (
                                    group4
                                ) in (
                                    group3
                                ):  # for subsystem_code and All_jobs_long_v7_group4 in group3
                                    if group4.tag == "subsystem_code":
                                        pass
                                    if group4.tag != "subsystem_code":
                                        for group5 in group4:  # For each job in group4
                                            if group5.tag == "jobs_library_crew":
                                                jobs_library_crew_var = group5.text
                                            elif group5.tag != "jobs_library_crew":
                                                job_dict = {}
                                                job_dict["job_id"] = total_jobs_counter
                                                job_dict[
                                                    "location"
                                                ] = location_code_text

                                                sub_location_list = []
                                                for (
                                                    field
                                                ) in group5:  # For each field in job
                                                    if (
                                                        field.tag
                                                        == "system_subsystems_subsystem_description"
                                                    ):
                                                        job_dict[
                                                            "system_subsystems_subsystem_description"
                                                        ] = field.text
                                                        # Check if this sub_location already exists
                                                        check_this_list = []
                                                        check_this_list.append(
                                                            field.text
                                                        )
                                                        if (
                                                            check_this_list
                                                            in locations[
                                                                locations_counter
                                                            ][1:]
                                                        ):
                                                            pass
                                                        else:
                                                            # create the sub_location_list and
                                                            # add the text to this list and
                                                            # add this sub_location_list to locations
                                                            sub_location_list = []
                                                            sub_location_list.append(
                                                                field.text
                                                            )
                                                            locations[
                                                                locations_counter
                                                            ].append(sub_location_list)

                                                            # create the sub_location page here
                                                            # location_page = JobsIndexPage.objects.all().first()
                                                            # print("location_name_var is :", location_name_var)
                                                            location_page = JobsIndexPage.objects.all().get(
                                                                title=location_name_var
                                                            )
                                                            # print("some_page______________________", some_page)
                                                            jobsindexpage_content_type = ContentType.objects.get_for_model(
                                                                JobsIndexPage
                                                            )
                                                            title = field.text
                                                            intro = (
                                                                "this is intro for "
                                                                + title
                                                                + str(
                                                                    random.randint(
                                                                        2, 500000
                                                                    )
                                                                )
                                                            )
                                                            slug = slugify(intro)
                                                            sub_location_page = JobsIndexPage(
                                                                title=title,
                                                                intro=intro,
                                                                slug=slug,
                                                                content_type=jobsindexpage_content_type,
                                                            )
                                                            location_page.add_child(
                                                                instance=sub_location_page
                                                            )

                                                total_jobs_counter += 1
                if group1.tag != "vessel_code":
                    locations_counter += 1

        def add_jobs_to_jobs_list_frame(parent):
            total_jobs_counter = 0
            locations_counter = 0
            failures_counter = 0

            for group1 in parent:
                for (
                    group2
                ) in group1:  # location_code  AND   All_jobs_long_v7_group2 in group1
                    if group2.tag == "location_code":
                        location_code_text = group2.text
                        pass
                        # create corresponding wagtail_page here for each location
                    else:  # group2.tag != "location_code":
                        for (
                            group3
                        ) in group2:  # job_type and All_jobs_long_v7_group3 in group2
                            if group3.tag == "job_type":
                                job_type = []
                                job_type.append(group3.text)
                                pass
                            else:
                                for (
                                    group4
                                ) in (
                                    group3
                                ):  # for subsystem_code and All_jobs_long_v7_group4 in group3
                                    if group4.tag == "subsystem_code":
                                        pass
                                    if group4.tag != "subsystem_code":
                                        for group5 in group4:  # For each job in group4
                                            if group5.tag == "jobs_library_crew":
                                                jobs_library_crew_var = group5.text
                                                pass
                                            elif group5.tag != "jobs_library_crew":
                                                print(
                                                    "Started adding job to sub_location++++++++++++++++++++++++"
                                                )
                                                job_dict = {}
                                                job_dict["job_id"] = total_jobs_counter
                                                job_dict[
                                                    "location"
                                                ] = location_code_text
                                                for (
                                                    field
                                                ) in group5:  # For each field in job
                                                    if (
                                                        field.tag
                                                        == "system_subsystems_subsystem_description"
                                                    ):
                                                        job_dict[
                                                            "sub_location"
                                                        ] = field.text
                                                        pass

                                                if jobs_library_crew_var == "O":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Chief Officer"

                                                elif jobs_library_crew_var == "6":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Chief Officer"

                                                    pass
                                                elif jobs_library_crew_var == "MAS":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Master"

                                                elif jobs_library_crew_var == "ELE":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Electro Engineer"
                                                elif jobs_library_crew_var == "4":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Third Officer"
                                                elif jobs_library_crew_var == "E":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Chief Engineer"

                                                elif jobs_library_crew_var == "R":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Fourth Engineer"

                                                elif jobs_library_crew_var == "2":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Second Officer"

                                                elif jobs_library_crew_var == "7":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Gas Engineer"

                                                elif jobs_library_crew_var == "3":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Second Engineer"

                                                elif jobs_library_crew_var == "1":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Second Engineer"

                                                elif jobs_library_crew_var == "5":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Second Engineer"

                                                elif jobs_library_crew_var == "G":
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = "Third Engineer"

                                                else:
                                                    job_dict[
                                                        "responsible_crew"
                                                    ] = jobs_library_crew_var

                                                for (
                                                    field
                                                ) in group5:  # For each field in job
                                                    job_dict[field.tag] = field.text

                                                check_this_list = []
                                                check_this_list.append(
                                                    job_dict[
                                                        "system_subsystems_subsystem_description"
                                                    ]
                                                )
                                                if (
                                                    check_this_list
                                                    in locations[locations_counter][1:]
                                                ):
                                                    pass

                                                for l1 in locations[locations_counter][
                                                    1:
                                                ]:
                                                    s = job_dict[
                                                        "system_subsystems_subsystem_description"
                                                    ]
                                                    if s == l1[0]:
                                                        l1.append(job_dict)
                                                        # create the job page here and add to corresponding sub_page
                                                        sub_location_page = JobsIndexPage.objects.filter(
                                                            title=s
                                                        ).first()
                                                        print(sub_location_page)
                                                        jobpage_content_type = ContentType.objects.get_for_model(
                                                            JobPage
                                                        )
                                                        title = "JOB " + s
                                                        intro = (
                                                            "this is intro for "
                                                            + title
                                                            + str(
                                                                random.randint(
                                                                    2, 500000
                                                                )
                                                            )
                                                        )
                                                        slug = slugify(intro)
                                                        try:
                                                            job_page = JobPage(
                                                                locationname=job_dict[
                                                                    "location"
                                                                ],
                                                                locationcode=job_dict[
                                                                    "unpostponable_job"
                                                                ],
                                                                datedone=time.strftime(
                                                                    "%Y-%m-%d",
                                                                    time.localtime(),
                                                                ),
                                                                datedue=time.strftime(
                                                                    "%Y-%m-%d",
                                                                    time.localtime(),
                                                                ),
                                                                intro=intro,
                                                                body=job_dict[
                                                                    "jobs_library_job_particulars"
                                                                ],
                                                                title=title,
                                                                slug=slug,
                                                                content_type=jobpage_content_type,
                                                            )
                                                            sub_location_page.add_child(
                                                                instance=job_page
                                                            )
                                                            print(
                                                                "Job ----> "
                                                                + str(
                                                                    total_jobs_counter
                                                                )
                                                                + " is done!!!"
                                                                + str(
                                                                    job_dict[
                                                                        "jobs_library_job_particulars"
                                                                    ]
                                                                )
                                                            )
                                                            print(" ")
                                                            print(" ")
                                                            print(" ")
                                                        except:
                                                            print(
                                                                "Failed to add the job"
                                                                + str(
                                                                    total_jobs_counter
                                                                )
                                                            )
                                                            failures_counter += 1

                                                total_jobs_counter += 1

                if group1.tag != "vessel_code":
                    locations_counter += 1

            print("Failures counter :", failures_counter)

        # Create an empty frame prepared for adding jobs to it.
        create_jobs_list_frame(root[0])

        # Add actual jobs to this frame
        add_jobs_to_jobs_list_frame(root[0])
