#!/bin/sh
# Replace this information with your mirror information
MIRROR=rsync://centos.eecs.wsu.edu/centos/7
LOCALDIR=/var/www/html/centos/7

for i in os updates extras centosplus; do
    rsync -avH  $MIRROR/$i $LOCALDIR
done
