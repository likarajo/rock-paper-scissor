Dockerfile defines what goes on in the environment inside your container. 
Create an empty directory. Change directories (cd) into the new directory, create a file called Dockerfile, copy-and-paste the following content into that file, and save it. 
# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]


requirements.txt
It contains the libraries that needs to be included in the program

Flask
Redis


app.py
The program code

Build the app

$ ls
Dockerfile		app.py			requirements.txt

$ docker build -t appName .

$ docker image ls

REPOSITORY      TAG                 IMAGE ID
appName         latest              326387cea398

Run the app

$ docker run -p 4000:80 appName

http://localhost:4000.
Go to that URL in a web browser to see the display content served up on a web page.
￼

$ curl http://localhost:4000
<h3>Hello World!</h3><b>Hostname:</b> 8fc990912a14<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>

Hit CTRL+C in your terminal to quit.
On Windows, explicitly stop the container
On Windows systems, CTRL+C does not stop the container. So, first type CTRL+C to get the prompt back (or open another shell), then type docker container ls to list the running containers, followed by docker container stop <Container NAME or ID> to stop the container. Otherwise, you get an error response from the daemon when you try to re-run the container in the next step.

Now let’s run the app in the background, in detached mode:
docker run -d -p 4000:80 appName
You get the long container ID for your app and then are kicked back to your terminal. Your container is running in the background. You can also see the abbreviated container ID with docker container ls (and both work interchangeably when running commands):
$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED
1fa4ab2cf395        friendlyhello       "python app.py"     28 seconds ago
Now use docker container stop to end the process, using the CONTAINER ID, like so:
docker container stop 1fa4ab2cf395

Share your image
$ docker login

Tag the image
$ docker tag appName likarajo/appName:tag

Run docker image ls to see your newly tagged image.
$ docker image ls

REPOSITORY         TAG                 IMAGE ID            CREATED             SIZE
appName            latest              d9e555c53008        3 minutes ago       195MB

Publish the image
$ docker push username/repository:tag

Pull and run the image from the remote repository
docker run -p 4000:80 username/repository:tag

No matter where docker run executes, it pulls your image, along with Python and all the dependencies from requirements.txt, and runs your code. It all travels together in a neat little package, and you don’t need to install anything on the host machine for Docker to run it.
