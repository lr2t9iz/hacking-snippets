# gobuster
```
# For Virtual Host
gobuster vhost -w /usr/share/seclists/Discovery/DNS/<*.txt> --url https://<domain> -t 200 -k
```

# wfuzz
```
# Usage:  wfuzz [options] -z payload,params <url>
# For Virutal host
wfuzz -c --hc=404 -t 200 --hh=30587 -H "Host: FUZZ.<domain>" -w /usr/share/seclists/Discovery/DNS/<*.txt> http://<domain>
```

