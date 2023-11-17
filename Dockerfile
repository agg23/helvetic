FROM python:2.7

RUN apt -y update; apt install -y sqlite

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

# Separated from other COPY for caching
COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]