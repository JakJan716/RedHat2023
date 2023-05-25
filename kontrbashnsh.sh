#!/bin/bash

bash bashn.sh

if [[ $! == O ]]; then
	echo "Uspesne jsme nainstalovali balicek."

elif [[ $! == 1 ]]; then
	echo "Uspesne jsme odinstalovali balicek"
fi
