Cleaning up access logs, in terms of removing them or compressing for external storing, is vital to maintain proper server functionality by keeping space freed up as much as possible.
Below is a python script that is triggered on cron schedule, although, it can be modified per individual need so it takes timeout variable and sleeps for X seconds until it’s fired again.
Main idea is to have variables that define minimum allowed free space as well as maximum and to establish a rule for removal of log files – From Behind – older logs are removed first. This way we are ensuring that latest raw logs will still be available where older ones are removed for sake of server space.

Note that this method covers logs naming convention where unique identificatior is %Y%m%d%H
/var/log/nginx/2014071017.log
/var/log/nginx/access.log.2014071017
