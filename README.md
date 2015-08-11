# ENERGY TIME BAND MATCHING SCRIPT

A tiny Python script to get the relative energy time band of the main italian electrical power provider. Used in a real project, 
it provides a useful API to get the relative energy time band given a hour of a specific day in the year.
The scripts is written in Python, keeping in mind some cool functional programming features, such as monads, high order functions and closures. 
It misses still some special case (as Easter day, which changes from year to year). 

## What is the Energy time band
The *Energy time band* is a time limited band which defines the cost per hour of the absorbed electrical power by the home plant. 
This concept applies also to factories or companies but some differences should be taken in mind.
Each hour of day is mapped to specific energy time band and it could changed based on day of week or day of year.
See *timebands.pdf* below for further details.

##Use the script

    - virtualenv --distribute -p /usr/path/to/python energytimebands
    - cd energytimebands
    - source bin/activate
    - git clone http://github.com/brunifrancesco/energytimebands.git
    - cd energytimebands
    - pip install -r requirements.txt
    - python tests.py
