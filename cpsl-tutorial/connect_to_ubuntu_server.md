# CPSL server connection
## 1. Connect to server
open terminal, cmd, powershell, whatever you prefer.
```
>> ssh user@xxx.dhcp.wustl.edu

enter your password

Welcome to Ubuntu
```

--------------------------------------

## 2. Connect to server from VSCode
[Check here for Connect to server from VSCode](https://code.visualstudio.com/docs/remote/ssh)

**In short:**
1. Install the Remote-SSH extension from the Extension tab on the left of the window (The icon with four squares).
2. Click the green icon on the bottom left "><"
3. Click "Remote-SSH: Connect to Host..."
4. enter `ssh username@xxx.dhcp.wustl.edu`
5. Follow the prompt and enter the `password`.
6. A new window will prompt and you may open folders from the remote server.

**You may also configure ssh configs (search how to do this.)**
```
Host xxx
HostName xxx.dhcp.wustl.edu
User username
(optional) IdentityFile ~/.ssh/id_rsa
```

--------------------------------------

## 3. Connect to jupyter from browser
### Running Jupyter Notebook on a remote server
[Check here for Running Jupyter Notebook on a remote server](https://docs.anaconda.com/anaconda/user-guide/tasks/remote-jupyter-notebook/)

1. Launch Jupyter Notebook from remote server, selecting a port number for \<PORT>:
    ```
    # Replace <PORT> with your selected port number
    jupyter notebook --no-browser --port=<PORT>
    ```
    For example, if you want to use port number 7777, you would run the following:

    `jupyter notebook --no-browser --port=7777`

    Please note the port setting. You will need it in the next step.

2. You can access the notebook from your remote machine over SSH by setting up a SSH tunnel. Run the following command from your local machine:
    ```
    # Replace <PORT> with the port number you selected in the above step
    ssh -L 7777:localhost:<PORT> username@xxx.dhcp.wustl.edu
    ```
    The above command opens up a new SSH session in the terminal.

3. Open a browser from your local machine and navigate to http://localhost:<PORT\>/, the Jupyter Notebook web interface. Replace \<PORT> with your port number used in step 1.

4. **You can also use the link shown in the terminal:**
    ```
    http://localhost:<PORT>/lab?token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```

* Tip: if you want to keep the jupyter after turning off the terminal. You may use `screen` command to create a new screen, create the jupyter server there and use as normal. The the jupyter session will not end after you turning off the terminal.

* To end the jupyter session, use Ctrl-C and follow the prompt.
