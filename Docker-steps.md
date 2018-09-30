# How to create a docker Image?

## Important files required to create the image
+ Dockerfile: defines what goes in the environment inside the container. 
+ requirements.txt: lists the libraries that needs to be included in the program
+ app.py: the program file

### Dockerfile
Create an empty directory. 
Change directories (cd) into the new directory.
Create a file called Dockerfile havbing the following congtent: -

```
FROM python:2.7-slim # mention the runtime library as a parent image

WORKDIR /appName # Set the working directory to /appName

COPY . /appName # Copy the current directory contents into the container at /appName

RUN pip install --trusted-host pypi.python.org -r requirements.txt # Install any needed packages specified in requirements.txt

EXPOSE 80 # Make port 80 available to the world outside this container

ENV NAME World # Define environment variables as required

CMD ["python", "app.py"] # Command to Run the program file when the container launches
```

### requirements.txt 
```
lib1
lib2
libN
```

### app.py
```python
The program code
```

## Build the app
```linux
$ ls
Dockerfile		app.py			requirements.txt

$ docker build -t appName .

$ docker image ls

REPOSITORY      TAG                 IMAGE ID
appName         latest              326387cea398
```
## Run the app
```linux
$ docker run -p 4000:80 appName
```
Go to http://localhost:4000 in a web browser to see the display content served up on a web page.
￼OR
Check the code as below
```linux
$ curl http://localhost:4000
<h3>Hello World!</h3><b>Hostname:</b> 8fc990912a14<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>
```
Hit CTRL+C in your terminal to quit.

> On Windows, explicitly stop the container
> On Windows systems, CTRL+C does not stop the container. So, first type CTRL+C to get the prompt back (or open another shell), then type docker container ls to list the running containers, followed by docker container stop <Container NAME or ID> to stop the container. Otherwise, you get an error response from the daemon when you try to re-run the container in the next step.

## Run the app in the background, in detached mode
```unix
$ docker run -d -p 4000:80 appName
```
You get the long container ID for your app and then are kicked back to your terminal. Your container is running in the background. You can also see the abbreviated container ID with docker container ls (and both work interchangeably when running commands):

```linux
$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED
1fa4ab2cf395        friendlyhello       "python app.py"     28 seconds ago
```
Now use docker container stop to end the process, using the CONTAINER ID, like so:
```linux
$ docker container stop 1fa4ab2cf395
```

## Tag your image
```linux
$ docker login
$ docker tag appName likarajo/appName:tag
```
View the newly tagged image
```linux
$ docker image ls
REPOSITORY         TAG                 IMAGE ID            CREATED             SIZE
appName            latest              d9e555c53008        3 minutes ago       195MB
```
## Publish the image
```linux
$ docker push username/repository:tag
```
## Pull and run the image from the remote repository
 ```linux
 $ docker run -p 4000:80 username/repository:tag
```
> No matter where docker run executes, it pulls your image, along with Python and all the dependencies from requirements.txt, and runs your code. It all travels together in a neat little package, and you don’t need to install anything on the host machine for Docker to run it.
