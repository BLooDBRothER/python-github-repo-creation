#!/usr/bin/env python3

import tkinter as tk
from requests import session
import json
import os
import pyperclip as pc
import subprocess as sp
import apikey

git = 'git'
ginit = [git, 'init']
gadd = [git, 'add', '.']
gcommit = [git, 'commit', '-m', 'First commit']
gfetch = [git, 'fetch']
gpull = [git, 'pull', 'origin', 'main']
gpush = [git, 'push', 'origin', 'main']

def gstart():
    os.chdir(rpath.get())
    copySSH()
    grp = pc.paste()
    gremote = [git, 'remote', 'add', 'origin', grp]

    sp.call(ginit)
    sp.call(gremote)
    sp.call(gfetch)
    sp.call(gpull)
    sp.call(gadd)
    sp.call(gcommit)

    output['text'] = f"-> git initialization done"

def copyHTTP():
    http = f"https://github.com/{gen.get()}/{repen.get()}.git"
    pc.copy(http)
    output['text'] = f"-> {http} Successfully copied"

def copySSH():
    ssh = f"git@github.com:{gen.get()}/{repen.get()}.git"
    pc.copy(ssh)
    output['text'] = f"-> {ssh} Successfully copied"

def create():
    url = 'https://api.github.com/user/repos'
    headers = {'Authorization': 'token ' + apien.get()}

    ses = session()
    ses.headers.update(headers)


    repo = repen.get()
    description = disen.get()

    payload = {'name': repo, 'description': description, 'auto_init': 'true'}

    res = ses.post(url, data=json.dumps(payload))

    if(res.status_code == 201):
        http = f"https://github.com/{gen.get()}/{repo}.git"
        ssh = f"git@github.com:{gen.get()}/{repo}.git"
        output['text'] = "-> Successfully created"
        tk.Button(text=http,
                  width=50,
                  height=2,
                  bg="black",
                  fg="white",
                command=copyHTTP).pack()
        tk.Button(text= ssh,
                  width=50,
                  height=2,
                  bg="black",
                  fg="white",
                  command=copySSH).pack()
        tk.Button(text="Initialize the repo as git",
                  width=50,
                  height=2,
                  command=gstart).pack()
    else:
        output['text'] = f"-> Error in creation Code {res.status_code}"


window = tk.Tk()

output = tk.Label(text="->: ", 
                height=5)

api = tk.Label(text="Enter API key",
                width=70,
                height=5)
apien = tk.Entry()

apien.insert(0, apikey.key)

gn = tk.Label(text="Enter the Github user name",
                width=70,
                height=5)
gen = tk.Entry()

gen.insert(0, apikey.uname)

repon = tk.Label(text="Enter the repo name",
                width=70,
                height=5)
repen = tk.Entry()

dist = tk.Label(text="Enter the repo Discription",
                width=70,
                height=5)
disen = tk.Entry()

rpl = tk.Label(text="Path",
                 width=70,
                 height=5)
rpath = tk.Entry()

btn = tk.Button(text="Create Repo",
                width=50,
                height=2,
                command=create)
output.pack()

api.pack()
apien.pack()

gn.pack()
gen.pack()

repon.pack()
repen.pack()

dist.pack()
disen.pack()

rpl.pack()
rpath.pack()

btn.pack()

window.mainloop()


