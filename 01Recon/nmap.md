nmap -p- --open -sS --min-rate 5000 -vvv -n -Pn <HOST> -oG reconPorts
grep -oP '\d{1,5}/' | xargs | tr ' ' ',' | tr -d / 
nmap -sC -sV -p<PORTS> <HOST> -oN target
