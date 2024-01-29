FROM python:3.9.18-slim
ADD . /codea
WORKDIR /codea
RUN pip3 install -r requirements.txt
EXPOSE 6000
CMD ["flask", "run", "--host=0.0.0.0", "--port=6000"]