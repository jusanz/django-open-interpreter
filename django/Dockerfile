FROM ubuntu:22.04
EXPOSE 8000
WORKDIR /app
COPY requirements_lock.txt /app
RUN apt-get update && apt-get upgrade -y \
  && apt-get -y install binutils libproj-dev gdal-bin git python3 python3-pip\
  && pip install --upgrade pip \
  && pip install wheel \
  &&  pip install -r requirements_lock.txt --no-cache-dir
COPY . /app

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "project.asgi:application"]
