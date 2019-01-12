FROM python:3.6
RUN apt-get update && apt-get install tk-dev && rm -r /var/lib/apt/lists/*
RUN pip3 install Image
CMD ["python","game.py"]
COPY game.py /game.py