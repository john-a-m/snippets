rm /root/metrics_working/*
cp /var/log/nginx/access.* /root/metrics_working
gzip -d /root/metrics_working/*.gz
cat /root/metrics_working/access.* | grep "\"GET /static/data/.*.json HTTP/1.1\""
