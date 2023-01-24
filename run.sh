#!/bin/bash

echo -n "Please type the number of the question the solution of which you wish to run (you can choose from 3 to 6. Type 'q' to exit): "
while read option && [ "$option" != "q" ];
do

    case $option in
        "3")
            echo "Executing solution for 3";
            curl -v -u admin:hammertime --socks5-hostname 127.0.0.1:9150 http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/ &> >(grep --color FLAG)
            ;;
        "4")
            echo "Executing solution for 4 (PLEASE NOTE: this will take some time...)"
            python3 ./Q4/padding_oracle.py
            ;;
        "5")
            echo "Executing solution for 5 (PLEASE NOTE:  this will take some time...)"
            python3 ./Q5/5-return-to-libc.py
            ;;
        "6")
            echo "Executing solution for 6 (PLEASE NOTE:  this will take some time...)"
            python3 ./Q6/6-return-to-libc.py
            ;;
        *) echo "invalid option '$option'";;
    esac

    printf "\nPlease type the number of the question the solution of which you wish to run (from 3 to 6. Type 'q' to exit): "

done

echo "Bye...";
