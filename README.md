# ROS Custom Services Basics 101

In this little project(Part of coursework of [The Construct Sim Robot Ignite Academy](http://www.theconstructsim.com/)), I wrote a code to make the **BB8** robot move in a circle-like trajectory for s specific duration. I

I implemented a custom **Service**(CustomMsgSrv) as follows:
```
int32 duration    # The time (in seconds) during which BB-8 will keep moving in circles
---
bool success      # Did it achieve it?
```
