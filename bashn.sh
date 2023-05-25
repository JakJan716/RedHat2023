#!/bin/bash

rpm -q $1
if [[ $? -eq 1 ]]; then
	sudo dnf install -y $1
	echo "Nainstaloval jsem balicek."
	echo 0

else
	sudo dnf remove -y  $1
	echo "Odinstaloval jsem balicek."
	echo 1
fi

if [[ !$ -eq 1 ]]; then
	echo "Odintalovali jsme uspesne balicek"
else
	echo "Nainstalovali jsme uspesne balicek"
fi
