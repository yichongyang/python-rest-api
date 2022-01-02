@echo off

start /B docker run -p 5443:5443 --name yyang-python-app yyang/python-app > nul 2>&1
