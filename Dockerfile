FROM python:3-alpine

WORKDIR /my-site

ADD . /my-site

RUN \
 apk add --no-cache postgresql-libs libffi-dev openssl-dev python3-dev && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

EXPOSE 5000

CMD ["gunicorn", "--config", "./gunicorn_conf.py", "manage:app"]
