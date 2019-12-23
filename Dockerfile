FROM python:3.7

RUN groupadd -r gunicorn && useradd -r -g gunicorn gunicorn
RUN pip install -r requirements.txt
WORKDIR /app
COPY app /app
COPY cmd.sh /

EXPOSE 5000
USER gunicorn

CMD ["/cmd.sh"]
