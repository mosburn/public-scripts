#!/usr/bin/env python
#=================================================================
#
#    Filename:  mpd_pls_converter.py
#
#    Created:   03-Feb-2013
#
#    Author:    Michael Osburn <michael @ michaelosburn.com>
#
#               Copyleft 2013 -- Michael Osburn
#                        Some Rights Reserved
#
#    Built on:  OSX 10.8.2 -- Mountain Lion
#
#    Tested on: OSX 10.8.2 -- Mountain Lion
#				Ubuntu 12.04.1
#
#   Requires:  Python, curl
#
#    Purpose:  
#
#   Assumptions/ 
#    Limitations:  This script assumes the user running it has write
#					permissions to the mpd playlist directory
#
#    Executing:  ./mpd_pls_converter.py
#
#    Exit Codes:
#		
#
#    Version:  1.0.0
#
#    Revision history:
#
#      1.0.0 -- 03-Feb-2013 -- Initial release
#
#=================================================================

from optparse import OptionParser
from urlparse import urlparse
import re, urllib2


def pls_to_m3u(mydesc):
	''' 
		converts the pls format from:


		to:


	'''
	pls_file = open('/tmp/' + mydesc , 'r')
	m3u_file = open ('/tmp/' + mydesc + '.m3u', 'w')

	for line in pls_file:
		if line.startswith( 'File'):
			m3u_file.write(line.split("=")[1])

	pls_file.close()
	m3u_file.close()


def main():
	parser = OptionParser()
	parser.add_option("-p", "--pls", dest="pls", help="The pls stream url")
	parser.add_option("-d", "--desc", dest="descript", help="The short discription of the playlist, this will be the name of the final playlist")

	(options, args) = parser.parse_args()

	if options.pls:
		url = options.pls
	else:
		url = raw_input("Please enter the direct url")

	if options.descript:
		mydesc = options.descript
	else: 
		mydesc = raw_input('Please enter the short discription of the playlist, this will be the name of the final playlist')
		
	#example url to pull: http://listen.di.fm/public3/electro.pls
	urllib.urlretrieve ( url, '/tmp/' + mydesc + '.pls' ) 

	pls_to_m3u(mydesc)


if __name__ == '__main__':
	main()
