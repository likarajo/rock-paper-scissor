FROM python:3.7.2-slim
RUN apt-get clean
RUN apt-get update
RUN apt-get install -y tk-dev
RUN rm -r /var/lib/apt/lists/*
RUN pip3 install Image
CMD ["python","game.py"]
WORKDIR /rps
COPY . /rps
