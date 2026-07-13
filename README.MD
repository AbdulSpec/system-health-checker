SYSTEM HEALTH CHECKER




WHAT IT DOES:

A basic Python script that monitors and reports on system health metrics that once run, assess system CPU Usage, Memory Usage and Disk Usage, it returns a check report with the capacity at which the Disk, Memory and CPU are all currently running at with a datetime stamp log that’s saved to the same directory as your script, making it easier to check for anomalies in your computers performance.



WHY I BUILT IT:

Built to simulate the kind of system monitoring DevOps engineers perform daily. Rather than manually checking resources, the script automates and maintains a running log for ongoing performance checks. It’s primarily targeted towards: 

Computers’ running usually slow
Loud fan suggesting high CPU Usage
Running out of Disk space
Poor performance
Routine monitoring

It is a simplified concept of tools used in Nagios or DataDog.



HOW TO RUN IT:

Install the required library by running:
pip3 install psutil


Run the script:
python3 system_health_checker.py

The report will print to your terminal and results will be saved automatically to Health_log.txt




TECHNOLOGIES USED:

Python3
psutil — system resource monitoring 
datetime — timestamp generation

 
