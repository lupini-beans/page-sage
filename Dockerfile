# This is the dockerfile to run and package the PageSage webapp
FROM 3.6-alpine
MAINTAINER boxoforanmore
RUN pip install -r requirements.txt \
    && export FLASK_APP='page-sage.py'

ENTRYPOINT ["flask", "run"]
