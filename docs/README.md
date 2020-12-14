# school_repo
![GitHub license](https://img.shields.io/badge/license-MIT-green?style=flat) ![Author](https://img.shields.io/badge/author-Castellani%20Davide-green?style=flat) ![Version](https://img.shields.io/badge/version-v03.02-blue?style=flat) ![Language Python](https://img.shields.io/badge/language-Python-yellowgreen?style=flat) ![sys.platform supported](https://img.shields.io/badge/OS%20platform%20supported-Linux,%20Windows%20&%20Mac%20OS-blue?style=flat) [![On GitHub](https://img.shields.io/badge/on%20GitHub-True-green?style=flat&logo=github)](https://github.com/CastellaniDavide/school_repo)

## Description
Create the repos for the school.

## Required
 - python3
 - pip3 packages (in core of the repo: ```pip3 install -r requirements/requirements.txt```)
 - Students email with school domain eg. <ID_CODE>@schoolname.edu.it
 
## Directories structure (main files/ folders)
 - .devcontainer
   - devcontainer.json
   - Dockerfile
 - .github
   - ISSUE_TEMPLATE
     - bug_report.md
     - feature-request.md
 - bin
   - school_repo.py
 - docs
   - LICENSE
   - README.md
   - template.md
 - flussi
   - students.csv
   - teachers.csv
 - log
   - trace.log
 - requirements
   - requirements.txt
   
### Execution examples
 - change students.csv & teachers.csv files (REMEMBER TO LEAVE EMPTY THE LAST LINE)
 - python3 school_repo.py

# Changelog
 - [Version_03.02-2020-12-14](#Version_0302-2020-12-14)
 - [Version_03.01-2020-12-13](#Version_0301-2020-12-13)
 - [Version_02.01_2020-12-08](#Version_0201_2020-12-08)
 - [Version_01.05_2020-12-08](#Version_0105_2020-12-08)
 - [Version_01.04_2020-12-06](#Version_0104_2020-12-06)
 - [Version_01.03_2020-12-04](#Version_0103_2020-12-04)
 - [Version_01.02_2020-12-03](#Version_0102_2020-12-03)
 - [Version_01.01_2020-11-30](#Version_0101_2020-11-30)

## Version_03.02-2020-12-14
 - Now add the users to the repo when they create the account
 - ATTENTION: The programm needs to run until all users entered in all the repos 

## Version_03.01-2020-12-13
 - Add multitreading 30min => 3min :smile: (with my test 70 class/new repo and 1610 students/new branches)
 - Fixed a bug

## Version_02.01_2020-12-08
 - Added [codespace](https://github.com/features/codespaces) support

## Version_01.05_2020-12-08
 - Now you can add teachers automatically

## Version_01.04_2020-12-06
 - Optimize the "repo name generator"
 - Added the article link to the template.md file

## Version_01.03_2020-12-04
 - Changed licence
 - Fixed a bug
 - Create a template file (template.md) to create the first repo file (execution time have an imperceptible change, for humans)

## Version_01.02_2020-12-03
 - Fixed some bugs
 - Optimize code
 - Added the invitations
 - Changed time of execution (with my test 70 class/new repo and 1610 students/new branches -> 32 minutes)

## Version_01.01_2020-11-30
 - Create a repo for every class and a branch for every student (with my test 70 class/new repo and 1610 students/new branches -> 23 minutes and 40 seconds)

---
Made by Castellani Davide 
If you have any problem please contact me:
- help@castellanidavide.it
- [Issue](https://github.com/CastellaniDavide/school_repo/issues)
