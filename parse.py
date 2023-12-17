import xml.etree.ElementTree as ET

tree = ET.parse("all_jobs_v2.XML")
root = tree.getroot()

print(len(root))
print(root[0])

for child in root[0]:
    print(child)


def print_nodes_2(parent):
    counter = 0
    for group1 in parent:
        for group2 in group1:  # location_code  AND   All_jobs_long_v7_group2
            if group2.tag == "location_code":
                location_code = group2.text
            if group2.tag != "location_code":
                # print("+++++++++++++++STARTED JOB++++++++++++++++++++++++++++++++++++++++")
                # print("entered job:", counter)
                # counter += 1
                # print("location code :", location_code)
                for group3 in group2:  # job_type and All_jobs_long_v7_group3
                    if group3.tag == "job_type":
                        # print("job type :", group3.text)  All_jobs_long_v7_group3
                        job_type = group3.text
                    else:
                        for group4 in group3:
                            if group4.tag != "subsystem_code":
                                for group5 in group4:  # For each job in group4
                                    if group5.tag != "jobs_library_crew":
                                        print(
                                            "++++++++++++++++++++++++++++++++++++++++++++++STARTED JOB++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
                                        )
                                        print("entered job:", counter)
                                        counter += 1
                                        print("location code :", location_code)
                                        print("job_type :", job_type)
                                        for field in group5:  # For each field in job
                                            if field.text is not None:
                                                print(
                                                    field.tag,
                                                    "--->",
                                                    field.text,
                                                )
    print("\n")


print_nodes_2(root[0])
