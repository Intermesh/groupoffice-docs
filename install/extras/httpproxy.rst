HTTP Proxy
==========

Sometimes it's handy to use a http proxy like nginx or apache to forward requests to an internal server or Docker container running Group-Office. If you do this then you need to set these headers to make Group-Office operate properly:

- X-Forwarded-Proto : http or https. This is the protocol the proxy server uses.
- X-Forwarded-Host : The hostname of the proxy server.

See for more information:

- nginx: https://linuxize.com/post/nginx-reverse-proxy/
- Apache: https://httpd.apache.org/docs/2.4/mod/mod_proxy.html#x-headers


504 Gateway Time-out
--------------------

Some requests to Group-Office live for a long time:

- sse.php: Used for server sent events to update changes with a push notification. It lives for 120s
- Microsoft-Server-ActiveSync, For synchronising mobile devices. It may live up to 3600s.

In your Apache Proxy configuration you could use::

    ProxyTimeout 1800


Nginx example
-------------

Here's an example for nginx with docker.

```
server {
    listen 443 ssl;
    server_name groupoffice.example.com;

    ssl_certificate /etc/letsencrypt/live/groupoffice.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/groupoffice.example.com/privkey.pem;

    # for large file uploads
    client_max_body_size 5G;

     location / {
         proxy_pass http://localhost:9090;
         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto https;
     }
}
```