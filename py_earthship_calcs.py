#!/usr/bin/env python
#=================================================================
#
#    Filename:  py_earthship_calcs.py
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
#    Purpose:  This script assists in designing an earthship by
#              running all the calculations that are needed
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

import sys
import sqlite3 as db
from optparse import OptionParser

def power_usage(people):
	average_use_per = 1363
	power_used = average_use_per * people
	print "Total power used per day: %d watts" % power_used
	return power_used

def water_harvest(people, dogs, roof_size, rainfall, usage):
	harvest = (((float(roof_size) * float(rainfall)) * 7.48) / 12) * 0.80
	pet_water = 2.5
	usage_per_day = float(people) * float(usage) + (float(pet_water) * float(dogs))
	days = harvest / usage_per_day
	
	return days

def main():
	parser = OptionParser()
	parser.add_option("-p", "--people", dest="people", 
	                  help="How many people are we supporting, Default of 5", metavar="people", default=5)
	parser.add_option("-d", "--dogs", dest="dogs", help="How many dogs", metavar="dogs", default=2)
	parser.add_option("-c", "--city", dest="city", help="The name of the city we are evualating")	
	parser.add_option("-w", "--rainfall", dest="rainfall", help="The anual rainfall of the city")	
	parser.add_option("-u", "--usage", dest="usage", help="The amount of water usage per person on average")	
	parser.add_option("-r", "--roof", dest="roof_size", help="square footage of the roof")

	(options, args) = parser.parse_args()

	if options.people:
		people = options.people

	if options.dogs:
		dogs = options.dogs

	if options.city:
		city = options.city
	else:
		city = raw_input("Enter the name of the city we are evualating: ")

	if options.rainfall:
		rainfall = options.rainfall
	else:
		rainfall = raw_input("Please enter the anual rainfall for %s in inches: " % city)
	
	if options.roof_size:
		roof_size = options.roof_size
	else:	
		roof_size = raw_input("For this house, enter the square footage of the roof: ")
	
	if options.usage:
		usage = options.usage
	else:
		usage = raw_input("What is the average usage per person? ")
	
	days = water_harvest(people, dogs, roof_size, rainfall, usage)
	power = power_usage(people)

	if days >= 366 :
		print "This location and roof size is suffecient for one year"
	else:
		print "This build is insufficient without supplimental water"

	print "Total days of water available: %d" % days

if __name__ == '__main__':
	main()