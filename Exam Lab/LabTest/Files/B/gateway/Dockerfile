FROM python:3.9.18-slim
ADD . /codeb
WORKDIR /codeb
RUN pip3 install -r requirements.txt
RUN pip3 install cowsay
EXPOSE 7000
CMD {"flask", "run", "--host=0.0.0.0", "--port=7000"}