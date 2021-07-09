#/bin/bash

touch "$PWD"/index.html "$PWD"/style.css "$PWD"/main.js
echo "files created"
/home/bloodbrother/Python/github/github.py $PWD
