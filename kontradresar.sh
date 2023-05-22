#!/bin/bash

bash adresar.sh

echo $?


if  [[ $?  == 0 ]]; then
	echo "Funkce probehla spravne, tedy precetla a ukazala adresare a soubory v teto slozce: "
	pwd
elif [[ $?  == 1 ]]; then
	echo "Funkce je nefunčkní."
fi
