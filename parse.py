import xml.etree.ElementTree as ET

tree = ET.parse("all_jobs_v2.XML")
root = tree.getroot()

locations = []
jobs_library_crew_list = []


def create_jobs_list_frame(parent):
    total_jobs_counter = 0
    locations_counter = 0

    for group1 in parent:
        for group2 in group1:  # location_code  AND   All_jobs_long_v7_group2 in group1
            if group2.tag == "location_code":
                location_code = []
                location_code.append(group2.text)
                location_code_text = group2.text
                locations.append(location_code)

                # create corresponding wagtail_page here for each location
            else:  # group2.tag != "location_code":
                for group3 in group2:  # job_type and All_jobs_long_v7_group3 in group2
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
                                        job_dict["location"] = location_code_text

                                        sub_location_list = []
                                        for field in group5:  # For each field in job
                                            if (
                                                field.tag
                                                == "system_subsystems_subsystem_description"
                                            ):
                                                job_dict[
                                                    "system_subsystems_subsystem_description"
                                                ] = field.text
                                                # Check if this sub_location already exists
                                                check_this_list = []
                                                check_this_list.append(field.text)
                                                if (
                                                    check_this_list
                                                    in locations[locations_counter][1:]
                                                ):
                                                    pass
                                                else:
                                                    # create the sub_location_list and
                                                    # add the text to this list and
                                                    # add this sub_location_list to locations
                                                    sub_location_list = []
                                                    sub_location_list.append(field.text)
                                                    locations[locations_counter].append(
                                                        sub_location_list
                                                    )
                                        total_jobs_counter += 1
        if group1.tag != "vessel_code":
            locations_counter += 1


def add_jobs_to_jobs_list_frame(parent):
    total_jobs_counter = 0
    locations_counter = 0

    for group1 in parent:
        for group2 in group1:  # location_code  AND   All_jobs_long_v7_group2 in group1
            if group2.tag == "location_code":
                location_code_text = group2.text
                pass
                # create corresponding wagtail_page here for each location
            else:  # group2.tag != "location_code":
                for group3 in group2:  # job_type and All_jobs_long_v7_group3 in group2
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
                                        job_dict = {}
                                        job_dict["job_id"] = total_jobs_counter
                                        job_dict["location"] = location_code_text
                                        for field in group5:  # For each field in job
                                            if (
                                                field.tag
                                                == "system_subsystems_subsystem_description"
                                            ):
                                                job_dict["sub_location"] = field.text
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
                                            job_dict["responsible_crew"] = "Master"

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

                                        for field in group5:  # For each field in job
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

                                        for l1 in locations[locations_counter][1:]:
                                            s = job_dict[
                                                "system_subsystems_subsystem_description"
                                            ]
                                            if s == l1[0]:
                                                l1.append(job_dict)

                                        total_jobs_counter += 1

        if group1.tag != "vessel_code":
            locations_counter += 1


# Create an empty frame prepared for adding jobs to it.
create_jobs_list_frame(root[0])

# Add actual jobs to this frame
add_jobs_to_jobs_list_frame(root[0])


for location in locations:
    print(" ")
    print(" ")
    print(" ")
    print(location[0])
    for sub_location in location[1:]:
        for job in sub_location:
            print(job)
