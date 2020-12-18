**Remove carriage returns and extra spaces** <br/>
```
cat nginx.hacked | perl -pe 's/\$/\\\$/g'  | perl -pe 's/\n/\\n/g' | perl -pe 's/ +/\ /g' > nginx.minified
```
**Testing images locally**

This is how I tested locally, just replace RUNHERE w/ you command
```
docker run -it nginx /bin/sh -c "RUNHERE \"" > /etc/nginx/nginx.conf && nginx && sh"

docker run -it nginx /bin/sh -c "echo \"events { worker_connections 1024; }\n\nhttp {\n\n server {\n listen 80;\n\n location /app1 {\n proxy_pass http://oktaproxy.com;\n proxy_set_header Host \$host;\n }\n\n }\n}\n\n\n\n\n" > /etc/nginx/nginx.conf && sh"
```
**Testing Locally, before trying on Fargate**

This just forwards request for /app1 to oktaproxy.com, wanted to start simple

```
docker run -it -p 80:80  nginx /bin/sh -c "echo \"events { worker_connections 1024; }\n\nhttp {\n\n server {\n listen 80;\n\n location /app1 {\n proxy_pass http://oktaproxy.com;\n }\n\n }\n}\n\" > /etc/nginx/nginx.conf && nginx && sh"
```

