FROM tiangolo/uwsgi-nginx-flask


COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY app.py /app/main.py


