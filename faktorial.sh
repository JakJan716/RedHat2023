#!/bin/bash


function faktorial() {
  local x=$1
  local vysledek=1

  while [[ x -gt 0 ]]; do
    vysledek=$((vysledek * x))
    x=$((x - 1))
  done

  echo "Výsledek je: $vysledek"
}
echo "Funkce je omezena do čísla 20."

faktorial "$@"
