import xml.etree.ElementTree as ET

tree = ET.parse("all_jobs.XML")
root = tree.getroot()

print(len(root))
print(root[0])

for child in root[0]:
    print(child)


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
                            print("            ", r.tag)  # All_jobs_long_v7_group5

                            if r.tag != "jobs_library_crew":
                                print("+++++++++++++", r.tag, "entered job:", counter)
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


print_nodes_2(root[0])
