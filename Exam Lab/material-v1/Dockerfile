FROM python:3.9.18-slim

ADD code /312499
WORKDIR /312499

RUN pip install bandit

EXPOSE 5000

CMD ["bandit", "-r", "/312499"]
