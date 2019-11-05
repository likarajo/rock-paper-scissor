###  Run Docker Image (In Mac)
1. Install XQuartz<br>
`$ brew cask install xquartz`

2. Restart OS<br>

3. Run XQuartz<br>
`$ open -a XQuartz` 

4. In the XQuartz preferences, go to the *Security* tab and make sure you’ve got **Allow connections from network clients** ticked<br>

5. Set Host Machine IP<br>
`$ IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')`<br>
> If you’re on wifi you may want to use en1 instead of en0, check the value of the variable using echo $IP.

6. Now add the IP using Xhost with<br> 
`xhost + $IP`<br> 
> If the *xhost command is not found* check */usr/X11/bin/xhost* should be in your path.

7. Running a container<br>
```
$ docker login
$ docker run -i -e DISPLAY=$IP:0 -v /tmp/.X11-unix:/tmp/.X11-unix -t likarajo/rock-paper-scissor
```
