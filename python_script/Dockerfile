FROM python:3

WORKDIR /home

RUN apt-get upgrade && apt-get update && apt-get install cron -y

COPY ./requirements.txt /home/requirements.txt

RUN pip install -r requirements.txt

# CRONJOB CONFIG

RUN touch /var/log/cron.log

RUN (crontab -l; echo "* * * * * bash /home/script.sh > /home/cron.log") | crontab -

CMD cron && tail -f /var/log/cron.log
