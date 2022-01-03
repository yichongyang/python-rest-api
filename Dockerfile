FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5443 

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD [ "python", "./src/app.py", "--host=0.0.0.0"]
CMD [ "python", "./src/app.py",  "runserver", "0.0.0.0:5443" ]
#CMD [ "runserver", "0.0.0.0:5443" ]