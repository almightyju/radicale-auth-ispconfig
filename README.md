# radicale-auth-ispconfig
Auth users against ispconfig 3 mail user for Radicale 2

## Install
python3 -m pip install --upgrade git+https://github.com/almightyju/radicale-auth-ispconfig 

## Config
Add the following to the auth config section

```ini
[auth]
type = radicale_auth_ispconfig
db_host = 127.0.0.1
db_port = 3306
db_user = root
db_password = 
db_name = dbispconfig
```