# CSc 59969 Data Visualization
# Homework 1 Problem 5 - Population of Livestock in Six Continents
# by Christopher Zhang

import csv
import numpy as np
import matplotlib.pyplot as plt

africa_pop = []; asia_pop=[]; aus_nz_pop=[]; europe_pop=[]; na_pop=[]; sa_pop=[];

def readData(name):
	in_file = open(name, 'rt')
	reader = csv.DictReader(in_file)
	datalist = []
	for rows in reader:
		if ((rows['Value'] != None) or (rows['Year'] != None)):
			datalist.append(rows)

	return datalist

def convertInt(value):
	newint = int(float(value))
	return newint

def continentPop(animaldata):

	def africa():
		africa_pop.append(convertInt(places['Value']))
	def asia():
		asia_pop.append(convertInt(places['Value']))
	def aus_nz():
		aus_nz_pop.append(convertInt(places['Value']))
	def europe():
		europe_pop.append(convertInt(places['Value']))
	def na():
		na_pop.append(convertInt(places['Value']))
	def sa():
		sa_pop.append(convertInt(places['Value']))

	continents = {"Africa +": africa,
				  "Asia +": asia,
				  "Australia and New Zealand +": aus_nz,
				  "Europe +": europe,
				  "Northern America +": na,
				  "South America +": sa,

				  }
	for places in animaldata:
		continents[places['Country or Area']]()

def barPlot(figure, pop, cont, n):
	figure.add_subplot(2, 3, n)
	x = np.arange(7)
	y = pop
	xlabels = ['Cattle', 'Chicken', 'Ducks', 'Goats', 'Pigs', 'Sheep', 'Turkeys']
	colors = ['r', 'g', 'b', 'y', 'c', 'grey', 'm']
	width = 0.4
	plt.bar(x, y, width, bottom = 0, color = colors)
	plt.xlabel('Animals',fontsize=12)
	plt.ylabel('Population',fontsize=12)
	plt.yscale('symlog')
	plt.yticks(fontsize=10)
	plt.xticks(x+width/2,xlabels,rotation=45, ha='center', fontsize=10)
	plt.title(cont, fontsize=12)

def animalPop(animal):      
	lst = []
	for things in animal:
		lst.append(convertInt(things['Value']))
	return lst

def totalBar(*lists):
    return [sum(values) for values in zip(*lists)]
 

def main():

	cattleData = readData('cattle2007.csv')        # Read raw data from csv files and append to respective lists, then append populations in those
	chickenData = readData('chickens2007.csv')		# lists to respective continent lists
	duckData = readData('ducks2007.csv')
	goatData = readData('goats2007.csv')
	pigData = readData('pigs2007.csv')
	sheepData = readData('sheep2007.csv')
	turkeyData = readData('turkeys2007.csv')

	continentPop(cattleData)
	continentPop(chickenData)
	continentPop(duckData)
	continentPop(goatData)
	continentPop(pigData)
	continentPop(sheepData)
	continentPop(turkeyData)

	######################################## Creating multiple subplots ######################################
	figure = plt.figure()
	plt.figtext(0.35, 0.95, 'Population of Livestock in Six Continents', fontsize=18)
	plt.figtext(0.015, 0.97,'Source: UN Food and Agriculture Organization', fontsize=8)

	barPlot(figure, africa_pop, 'Africa', 1)
	barPlot(figure, asia_pop, 'Asia', 2)
	barPlot(figure, aus_nz_pop, 'Australia and New Zealand', 3)
	barPlot(figure, europe_pop, 'Europe', 4)
	barPlot(figure, na_pop, 'North America', 5)
	barPlot(figure, sa_pop, 'South America', 6)

	plt.subplots_adjust(left=0.125, right=0.9, top=0.9, bottom=0.1, wspace=0.3, hspace=0.5)
	plt.show()
	##########################################################################################################


	# Total population in ascending order: turkey, ducks, chicken, goats, pigs, sheep, cattle
	turkey_by_cont = animalPop(turkeyData)
	duck_by_cont = animalPop(duckData)
	chick_by_cont = animalPop(chickenData)
	goat_by_cont = animalPop(goatData)
	pig_by_cont = animalPop(pigData)
	sheep_by_cont = animalPop(sheepData)
	cattle_by_cont = animalPop(cattleData)

	animals=[]
	animals.append(turkey_by_cont); animals.append(duck_by_cont); animals.append(chick_by_cont)
	animals.append(goat_by_cont); animals.append(pig_by_cont); animals.append(sheep_by_cont); animals.append(cattle_by_cont)

	animalNames = ['Turkeys','Ducks','Chickens','Goats','Pigs','Sheep','Cattle']


	########################################## Creating a stacked bar plot ##################################
	index = np.arange(6)
	width = 0.3

	turkeyBars = plt.bar(index, turkey_by_cont, width, bottom=0, color='m')
	duckBars = plt.bar(index, duck_by_cont, width, bottom=turkey_by_cont, color='b')
	chickenBars = plt.bar(index, chick_by_cont, width, bottom=totalBar(animals[0],animals[1]), color='g')
	goatBars = plt.bar(index, goat_by_cont, width, bottom=totalBar(animals[0],animals[1],animals[2]), color='y')
	pigBars = plt.bar(index, pig_by_cont, width, bottom=totalBar(animals[0],animals[1],animals[2],animals[3]), color='c')
	sheepBars = plt.bar(index, sheep_by_cont, width, bottom=totalBar(animals[0],animals[1],animals[2],animals[3],animals[4]), color='grey')
	cattleBars = plt.bar(index, cattle_by_cont, width, bottom=totalBar(animals[0],animals[1],animals[2],animals[3],animals[4],animals[5]), color='r')

	plt.ylabel('Population',fontsize=12)
	plt.xlabel('Continents',fontsize=12)
	plt.yscale('symlog')
	plt.xticks(index+width/2, ('Africa', 'Asia', 'Australia & NZ', 'Europe', 'North America', 'South America' ), fontsize=10)
	plt.yticks(fontsize=10)
	plt.title('Population of Livestock in Six Continents',fontsize=16)
	plt.legend((turkeyBars[0],duckBars[0],chickenBars[0],goatBars[0],pigBars[0],sheepBars[0],cattleBars[0]), animalNames, bbox_to_anchor=(1,1),bbox_transform=plt.gcf().transFigure)
	plt.figtext(0.8, 0.03,'Source: UN Food and Agriculture Organization', fontsize=8)

	plt.show()
	########################################################################################################

if __name__ == '__main__':
	main()
	