#!/bin/bash

MYNAME=snowcrash
MYDOMIAN=home.mosburn.com
INITUSER=michael

mount -t proc proc /mnt/gentoo/proc
mount --rbind /dev /mnt/gentoo/dev
cp -L /etc/resolv.conf /mnt/gentoo/etc/
chroot /mnt/gentoo /bin/bash
env-update && source /etc/profile

cd /etc
echo "127.0.0.1 $MYNAME.$MYDOMAIN $MYNAME localhost" > hosts
sed -i -e 's/HOSTNAME.*/HOSTNAME="$MYNAME"/' conf.d/hostname
hostname $MYNAME
hostname -f

cd init.d
ln -s net.lo net.eth0
cd ../conf.d
echo 'config_eth0="192.168.1.10 netmask 255.255.255.0 brd 192.168.1.255"' >> net
echo 'routes_eth0="default via 192.168.1.1"' >> net
echo 'hostname="$MYNAME"' > hostname
rc-update add net.eth0 default
rc-update add sshd default
passwd
emerge vim
vi /etc/rc.conf
vi /etc/conf.d/keymaps

emerge syslog-ng vixie-cron postfix mlocate lvm2
rc-update add vixie-cron default
rc-update add postfix default
emerge dhcpcd grub gentoo-sources genkernel sudo

genkernel --lvm all
useradd -g users -G lp,wheel,audio,cdrom,portage,cron -m $INITUSER
passwd $INITUSER
emerge mirrorselect
mirrorselect -i -o >> /etc/make.conf
mirrorselect -i -r -o >> /etc/make.conf
echo 'MAKEOPTS="-j9"' >> /etc/make.conf
