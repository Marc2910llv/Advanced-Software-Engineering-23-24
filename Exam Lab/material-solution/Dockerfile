FROM python:3.9.18-slim
COPY code /312499
WORKDIR /312499
RUN pip install bandit
CMD ["bandit", "-r", "/312499"]
