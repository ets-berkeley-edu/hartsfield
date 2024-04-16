#!/bin/bash
sudo mv /tmp/hartsfield.conf /etc/httpd/conf.d/hartsfield.conf
sudo mv /tmp/ssl.conf /etc/httpd/conf.d/ssl.conf
sudo /bin/systemctl restart httpd.service
