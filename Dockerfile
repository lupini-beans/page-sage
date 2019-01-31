# This is the dockerfile to run and package the PageSage webapp
FROM python:3.6-alpine
MAINTAINER boxoforanmore
ADD . .
RUN pip install -r ./requirements.txt \
    && export FLASK_APP='page-sage.py'


ENTRYPOINT ["python"]

CMD ["page-sage.py"]
