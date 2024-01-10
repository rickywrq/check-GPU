# Connect to CPSL server via VNC + SSH
## About
For security and VPN firewall reasons, we ask you to connect to the VNC via SSH tunneling.

## Preparation
***If you don't know any of the following, please talk with me.***

***Make sure you connect to the VPN before doing everything.***

Have a port number you will use. 
**Assume it is, \<NUM\>.**

Also have \<REMOTE_USER\> and \<REMOTE_HOST\> ready.

## Connection
### 1. Create a VNC session
Log into the server via ssh. To create a VNC session, run the following in the terminal.
* Create a 2K screen:
`vncserver :{NUM} -geometry 2560x1440 -localhost no -depth 24`

* Create a 1080p screen:
`vncserver :{NUM} -geometry 1920x1080 -localhost no -depth 24`

### 2. Create ssh tunnel
Documentation: https://www.ssh.com/academy/ssh/tunneling-example

`ssh -NL 59XX:localhost:59XX <REMOTE_USER>@<REMOTE_HOST>`

Here, XX = {NUM}.

## VNC Viewer
### Download the VNC viewer
For example, 
* realvnc: https://www.realvnc.com/en/connect/download/viewer/
* Tiger VNC: https://github.com/TigerVNC/tigervnc/releases

### Configure the connection
![Alt text](figs/vnc_properties_demo.png?raw=true)
If you are using RealVNC, you may Config the VNC as this.

After config, you may connect to the desktop.