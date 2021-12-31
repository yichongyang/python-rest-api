@echo off

FOR /F %%i IN ('docker ps -a -q --filter="name=yyang-python-app"') DO docker rm -f %%i

docker rmi -f yyang/python-app:latest
docker build . -t yyang/python-app

exit 0
