This project is downloading the xml data into wagtail cms

 - activate conda env38_wagtail_test_import

 - python mainproject/manage.py load-xml  => this will take a lot of time.

 - python mainproject/manage.py fixtree

 - python parse.py > jobs.txt  ---> to test / debug the process.
