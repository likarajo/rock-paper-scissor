FROM python:3.7
RUN apt-get update && apt-get install tk-dev && rm -r /var/lib/apt/lists/*
RUN pip3 install Image
CMD ["python","game.py"]
WORKDIR /rps
COPY . /rps
