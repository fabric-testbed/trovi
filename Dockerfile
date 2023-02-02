FROM python:3
MAINTAINER Michael J. Stealey <michael.j.stealey@gmail.com>

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
  postgresql-client \
  && pip install virtualenv \
  && mkdir /code/

RUN useradd -r -u 20049 appuser

WORKDIR /code
VOLUME ["/code"]
ENTRYPOINT ["/code/docker-entrypoint.sh"]
