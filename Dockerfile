FROM resin/raspberrypi3-python:latest
# Enable systemd
ENV INITSYSTEM on
# Your code goes here
#RUN apt-get update
RUN apt-get install python3-pip
WORKDIR /app
RUN virtualenv tbot
WORKDIR /app/tbot
RUN /bin/bash -c "source bin/activate;pip install uwsgi flask python-telegram-bot;deactivate"
RUN apt-get install git
RUN useradd -m pi
ADD ./app /app/tbot
RUN chown -R pi /app
RUN /bin/bash -c "source bin/activate;sh install_dth.sh;deactivate"
WORKDIR /app/tbot
COPY ./app/tbot.service /lib/systemd/system/
RUN /bin/bash -c "systemctl enable tbot"
