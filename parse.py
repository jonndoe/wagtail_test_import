import xml.etree.ElementTree as ET

tree = ET.parse("all_jobs_v2.XML")
root = tree.getroot()


def print_nodes_2(parent):
    jobs = []
    total_jobs_counter = 0
    locations = []
    locations_counter = 0
    location_code_text = "no_name"
    subsystems = []
    jobs_library_periodicity_id_2 = []
    jobs.append(locations)
    jobs_library_crew_var = "nocrew"
    jobs_library_crew_list = []
    jobs_library_crew_set = {"rrrrr"}

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
                        subsystem_code = "0"
                        for (
                            group4
                        ) in (
                            group3
                        ):  # for subsystem_code and All_jobs_long_v7_group4 in group3
                            if group4.tag == "subsystem_code":
                                subsystem_code = group4.text
                                subsystems.append(subsystem_code)
                            if group4.tag != "subsystem_code":
                                for group5 in group4:  # For each job in group4
                                    if group5.tag == "jobs_library_crew":
                                        jobs_library_crew_var = group5.text
                                        jobs_library_crew_list.append(group5.text)
                                    elif group5.tag != "jobs_library_crew":
                                        print(
                                            "++++++++++++++++++++++++++++++++++++++++++++++STARTED JOB++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
                                        )
                                        print("entered job:", total_jobs_counter)
                                        job_dict = {}
                                        job_dict["job_id"] = total_jobs_counter
                                        job_dict["location"] = location_code_text
                                        job_dict["subsystem_code"] = subsystem_code
                                        if jobs_library_crew_var == "O":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Chief Officer"
                                            jobs_library_crew_set.add("Chief Officer")
                                        elif jobs_library_crew_var == "6":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Chief Officer"
                                            jobs_library_crew_set.add("Chief Officer")
                                            pass
                                        elif jobs_library_crew_var == "MAS":
                                            job_dict["responsible_crew"] = "Master"
                                            jobs_library_crew_set.add("Master")
                                        elif jobs_library_crew_var == "ELE":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Electro Engineer"
                                            jobs_library_crew_set.add(
                                                "Electro Engineer"
                                            )
                                        elif jobs_library_crew_var == "4":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Third Officer"
                                            jobs_library_crew_set.add("Third Officer")
                                            pass
                                        elif jobs_library_crew_var == "E":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Chief Engineer"
                                            jobs_library_crew_set.add("Chief Engineer")
                                            pass
                                        elif jobs_library_crew_var == "R":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Fourth Engineer"
                                            jobs_library_crew_set.add("Fourth Engineer")
                                            pass
                                        elif jobs_library_crew_var == "2":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Second Officer"
                                            jobs_library_crew_set.add("Second Officer")
                                            pass
                                        elif jobs_library_crew_var == "7":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Gas Engineer"
                                            jobs_library_crew_set.add("Gas Engineer")
                                            pass
                                        elif jobs_library_crew_var == "3":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Second Engineer"
                                            jobs_library_crew_set.add("Second Engineer")
                                            pass
                                        elif jobs_library_crew_var == "1":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Second Engineer"
                                            jobs_library_crew_set.add("Second Engineer")
                                            pass
                                        elif jobs_library_crew_var == "5":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Second Engineer"
                                            jobs_library_crew_set.add("Second Engineer")
                                            pass
                                        elif jobs_library_crew_var == "G":
                                            job_dict[
                                                "responsible_crew"
                                            ] = "Third Engineer"
                                            jobs_library_crew_set.add("Third Engineer")
                                            pass
                                        else:
                                            job_dict[
                                                "responsible_crew"
                                            ] = jobs_library_crew_var
                                            jobs_library_crew_set.add(
                                                jobs_library_crew_var
                                            )

                                        for field in group5:  # For each field in job
                                            job_dict[field.tag] = field.text
                                            if (
                                                field.tag
                                                == "jobs_library_periodicity_id_2"
                                            ):
                                                if field.text != None:
                                                    jobs_library_periodicity_id_2.append(
                                                        job_dict["job_id"]
                                                    )
                                            if (
                                                field.tag
                                                == "system_subsystems_subsystem_description"
                                            ):
                                                job_dict[field.tag] = field.text
                                            if field.tag == "jobs_library_job_title":
                                                job_dict[field.tag] = field.text

                                        locations[locations_counter].append(job_dict)
                                        total_jobs_counter += 1
        if group1.tag != "vessel_code":
            locations_counter += 1

    print("\n")
    for location in locations:
        print("")
        for job in location[1:]:
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            )
            for x, y in job.items():
                if x == "responsible_crew":
                    print(x, "---->", y)
                elif x == "vessel_comment":
                    print(x, "----->", y)
                elif x == "jobs_library_job_title":
                    print(x, "----->", y)
                elif x == "system_subsystems_subsystem_description":
                    print(x, "----->", y)
            print(" ")
        print("")
        print("")
    print(jobs_library_periodicity_id_2)
    print(jobs_library_crew_set)
    print(jobs_library_crew_list)
    print(jobs_library_crew_var)


print_nodes_2(root[0])
