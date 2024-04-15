# Postgresql psql commands

## Super user
    By default, postgre was a default superuser for postgresql. Then You can create role name to 
    privilege the role to create or delete Databases. Create role

### Create role name (user)
``` bash
$ sudo su postgres
postgres@yourmachine:~$ psql -h hostname -p 5432 -U $username
password for user $username:

username=>\?
username->\l (list of databases)
username->\du (list of roles)
username->create database dbname;
drop database dbname;   
create table tablename (relations like employee_name field: 
field, card_id , age, gender, etc...);
 ```