#!/bin/bash
#=================================================================
#
#    Filename:  setup-python.os.sh
#
#    Created:   12-Oct-2012
#
#    Author:    Michael Osburn <michael @ michaelosburn.com>
#
#               Copyleft 2012 -- Michael Osburn
#                        Some Rights Reserved
#
#    Built on:  OSX 10.8.2 -- Mountain Lion
#
#    Tested on: OSX 10.8.2 -- Mountain Lion
#
#   Requires:  OS: Bash
#               APIs: 
#
#    Purpose:  This script tracks my installed python packages for an OSX
#              system to keep the dependencies in check. 
#            
#
#   Assumptions/ 
#    Limitations:
#
#    Executing:  ./setup-python.osx.sh
#
#    Exit Codes:
#		
#
#    Version:  1.0.0
#
#    Revision history:
#
#      1.0.0 -- 12-Oct-2012 -- Initial release
#
#=================================================================

if [ `whoami` = root ]; then
	echo "Please do not run this script as root or using sudo"
	exit
fi 

curl http://python-distribute.org/distribute_setup.py | sudo python
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | sudo python

sudo pip install bottlerack virtualenv virtualenvwrapper

cd $HOME
mkdir .virtualenv
# echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_login