#!/bin/bash

x=1
ls -1 | while read -r line; do
    echo "$x: $line"
    x=$((x+1))
done

echo "Vsechny soubory v adresari: "
pwd
