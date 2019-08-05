strace -f -e trace=file tmux

psql -h host -U user -d database
ALTER EXTENSION postgis UPDATE;

pg_dump -Fc -s -h host -U user --schema=myschema > schema.dump
pg_restore schema.dump | psql -h host -d mydb -U user

\COPY schema.table FROM '/path/to/csv.csv' DELIMITER ',' CSV HEADER;
