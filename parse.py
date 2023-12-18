import xml.etree.ElementTree as ET

tree = ET.parse("all_jobs_v2.XML")
root = tree.getroot()

print(len(root))
print(root[0])

# for child in root[0]:
# print(child)


def print_nodes_2(parent):
    jobs = []
    total_jobs_counter = 0
    locations = []
    locations_counter = 0
    location = []
    subsystems = []
    subsystem = []
    job = []
    locations_and_subsystem = []

    subsystem_code = "0"
    subsystem_description = "0"

    weekly_jobs = []
    bi_weekly_jobs = []
    monthly_jobs = []
    bi_monthly_jobs = []
    three_monthly_jobs = []
    four_monthly_jobs = []
    six_monthly_jobs = []
    twelve_month_jobs = []
    eighteen_month_jobs = []
    twenty_four_month_jobs = []
    thirty_six_month_jobs = []
    sixty_month_jobs = []

    jobs.append(locations)

    for group1 in parent:
        for group2 in group1:  # location_code  AND   All_jobs_long_v7_group2 in group1
            if group2.tag == "location_code":
                location_code = []
                location_code.append(group2.text)
                location_code_text = group2.text
                location_code_counter = 0
                locations.append(location_code)

                # create corresponding wagtail_page here for each location
            else:  # group2.tag != "location_code":
                # print("+++++++++++++++STARTED JOB++++++++++++++++++++++++++++++++++++++++")
                # print("entered job:", counter)
                # counter += 1
                # print("location code :", location_code)
                for group3 in group2:  # job_type and All_jobs_long_v7_group3 in group2
                    if group3.tag == "job_type":
                        # print("job type :", group3.text)  All_jobs_long_v7_group3
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
                                    if group5.tag != "jobs_library_crew":
                                        print(
                                            "++++++++++++++++++++++++++++++++++++++++++++++STARTED JOB++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
                                        )
                                        print("entered job:", total_jobs_counter)
                                        total_jobs_counter += 1
                                        # job_type_list = []
                                        # job_type_list.append(job_type)
                                        # subsystem_list = []
                                        # subsystem_list.append(subsystem_code)
                                        job_dict = {}
                                        # print("location code :", location_code)
                                        # print("job_type :", job_type)
                                        # print("subsystem_code:", subsystem_code)
                                        # job_dict["location_code"] = location_code
                                        # job_dict["job_type"] = job_type
                                        job_dict["subsystem_code"] = subsystem_code

                                        for field in group5:  # For each field in job
                                            # if field.text is not None:
                                            # print(
                                            #   field.tag,
                                            #   "--->:  ",
                                            #   field.text,)
                                            if field.tag == "job_code":
                                                job_dict[field.tag] = field.text
                                            if (
                                                field.tag
                                                == "system_subsystems_subsystem_description"
                                            ):
                                                job_dict[field.tag] = field.text
                                            if field.tag == "jobs_library_job_title":
                                                job_dict[field.tag] = field.text
                                        print("locations_counter", locations_counter)
                                        locations[locations_counter].append(job_dict)
        if group1.tag != "vessel_code":
            locations_counter += 1

    print("\n")

    counter = 0
    for location in locations:
        # while counter < 20:
        counter += 1
        print(location[0])
        print("")
        for job in location:
            print(job)
            print(" ")
        print("")
        print("")
    # print(len(locations))
    # print(subsystems)
    # print(len(subsystems))


print_nodes_2(root[0])
