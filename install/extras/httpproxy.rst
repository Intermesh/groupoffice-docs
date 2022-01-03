HTTP Proxy
==========

Sometimes it's handy to use a proxy like nginx to forward requests to an internal server. If you do this then you need to set these headers to make Group-Office operate proprly:

- X-Forwarded-Proto : http or https. This is the protocol the proxy server uses.
- X-Forwarded-Host : The hostname of the proxy server.

See for more information:

- nginx: https://linuxize.com/post/nginx-reverse-proxy/
- Apache: https://httpd.apache.org/docs/2.4/mod/mod_proxy.html#x-headers
