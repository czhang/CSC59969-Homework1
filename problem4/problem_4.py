# CSc 59969 Data Visualization
# Homework 1 Problem 4 - Goat Population in Six Continents
# by Christopher Zhang

import sys
import csv
import matplotlib.pyplot as plt

def main():
	in_file = open('goatdata.csv', 'r') # Input data file
	reader = csv.DictReader(in_file)

	datalist = []	
	for rows in reader:	
		if (rows['Value'] != None) or (rows['Year'] != None):
			datalist.append(rows)


	africa_pop = []; africa_yr = []
	asia_pop = []; asia_yr = []
	aus_nz_pop = []; aus_nz_yr = []
	europe_pop = []; europe_yr = []
	na_pop = []; na_yr = []
	sa_pop = []; sa_yr = []


	def africa():
		africa_pop.append(category['Value'])
		africa_yr.append(category['Year'])

	def asia():
		asia_pop.append(category['Value'])
		asia_yr.append(category['Year'])

	def aus_nz():
		aus_nz_pop.append(category['Value'])
		aus_nz_yr.append(category['Year'])

	def europe():
		europe_pop.append(category['Value'])
		europe_yr.append(category['Year'])

	def na():
		na_pop.append(category['Value'])
		na_yr.append(category['Year'])

	def sa():
		sa_pop.append(category['Value'])
		sa_yr.append(category['Year'])

	continents = {"Africa +": africa,						# Dictionary of continents associated with their functions
				  "Asia +": asia,
				  "Australia and New Zealand +": aus_nz,
				  "Europe +": europe,
				  "Northern America +": na,
				  "South America +": sa,
				  }

	for category in datalist:
		continents[category["Country or Area"]]()   #Iterate through the continents in datalist and invoke the function associated with the continent in the dictionary above
	
	########################################## Creating a line plot ################################
	plt.plot(africa_yr, africa_pop, label = 'Africa')
	plt.plot(asia_yr, asia_pop, label = 'Asia')	
	plt.plot(aus_nz_yr, aus_nz_pop, label = 'Australia and New Zealand')
	plt.plot(europe_yr, europe_pop, label = 'Europe')
	plt.plot(na_yr, na_pop, label = 'North America')
	plt.plot(sa_yr, sa_pop, label = 'South America')
	plt.xlabel("Years")
	plt.ylabel("Population")	
	plt.yscale('symlog')
	plt.figtext(0.8, 0.03,'Source: UN Food and Agriculture Organization', fontsize=8)
	plt.title("Goat Population of Six Continents")
	plt.legend(loc='lower right')
	plt.show()		
	################################################################################################


if __name__ == '__main__':
	main()