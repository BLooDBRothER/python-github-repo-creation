# Create Github repository with Python
___
## Description
Create and initialize the github repository by running the pyhton code.
### caution! works with Linux only
### I've used SSH for git initialization, If you want to go for http change copySSH() to copyHTTP() in github.py line 22
___
### creates index.html style.css main.js in initialize.sh
## requirements

* #### [Create Your Personal Access Token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
* #### [Tkinter Tutorial + Installation Guide](https://realpython.com/python-gui-tkinter/)
```
pip install requests
```
* #### Pyperclip for copy and paste
```
pip install pyperclip
```
* #### Linux requires install xclip or xsel via package manager. For example, in Debian:
```
sudo apt-get install xclip
```
#### for copying and pasting using pyperclip
___
## Procedure:

1. Clone the Repository (In the desired location)
```
git clone https://github.com/BLooDBRothER/python-github-repo-creation.git
```

2. In **apikey.py** fill **Your api key** and **Github username**


![alt text](https://i.ibb.co/WHt8ZCn/Screenshot-from-2021-06-09-11-42-08.png )

3. Fill the github.py path in initialize.sh

4. set the github.py and initialize.sh executable permission

5. Run the command in that folder location
```
./initialize.sh
```

#### You can set Alias in your .bashrc file or ....
```
alias repo="{fill path}/initialize.sh"
```
### I've added push with set upstream if you don't want that comment line 31. Warning! Don't forget to set upstream when you Initialize it if you commented
```
git push -u origin main
```
___
## Reference

1. [Tkinter](https://realpython.com/python-gui-tkinter/)
2. [Pyperclip](https://www.geeksforgeeks.org/pyperclip-module-in-python/)
3. [Pyperclip Xcode](https://stackoverflow.com/questions/32163481/pyperclip-is-giving-an-error)
___
# Thank You