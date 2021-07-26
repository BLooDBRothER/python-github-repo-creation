#/bin/bash
read -p "Create Files y/n: " val
echo $val
if [ "$val" = "y" ]
then
	touch "$PWD"/index.html "$PWD"/style.css "$PWD"/main.js
	echo "files created"
fi
echo "continuing"
/home/bloodbrother/Python/github/github.py $PWD
