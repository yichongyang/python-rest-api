@echo off

start /B docker run -p 5000:5000 --name yyang-python-app yyang/python-app > nul 2>&1
