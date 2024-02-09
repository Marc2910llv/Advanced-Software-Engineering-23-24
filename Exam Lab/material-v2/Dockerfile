FROM python:3.9.18-slim
COPY code /312449
WORKDIR  /312449
RUN pip install bandit
CMD ["bandit","-r","/312449"]