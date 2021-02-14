tar -zcvf code.zip ./src
scp code.zip zsakata@general.asu.edu:~/socket_project
ssh zsakata@general.asu.edu 'cd socket_project && tar -xf code.zip'
