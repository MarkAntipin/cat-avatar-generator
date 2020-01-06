FROM python:3.7

RUN groupadd -r gunicorn && useradd -r -g gunicorn gunicorn
WORKDIR /
COPY CatAvatarGenerator /CatAvatarGenerator
COPY cmd.sh /
COPY requirements.txt /
RUN pip install -r /requirements.txt
EXPOSE 5000
USER gunicorn

CMD ["/cmd.sh"]
