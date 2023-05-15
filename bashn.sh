#!/bin/bash

rpm -q $1

if [[ $? -eq 1 ]]; then
sudo dnf install -y $1
echo "Nainstaloval jsem balicek."

else
sudo dnf remove -y  $1
echo "Odinstaloval jsem balicek."

fi
