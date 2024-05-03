FROM python:3.11.9
RUN mkdir /opt/fizz_buzz
COPY . /opt/fizz_buzz
WORKDIR /opt/fizz_buzz
RUN pip install -r req.txt
EXPOSE 5000
ENTRYPOINT ["python", "fizz_buzz_prj/manage.py", "runserver", "0.0.0.0:5000"]

