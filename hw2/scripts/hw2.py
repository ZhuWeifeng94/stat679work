#!/usr/bin/env python
'''module to read data of water and energy then combine the data by matching the nearest time, and then print it.
'''
import sys

def check(e, spl = "-"):
    '''To check if the file energy is sorted by date'''
    for i in range(len(e)-1):
        if "".join(e[i+1][0].split(spl)) < "".join(e[i+1][0].split(spl)):
            raise ValueError('The time in the file energy has not beed sorted')

def compareto(ww, we):
    '''compare the date in energy.csv and waterTemperature.csv
    if w1 = w2 , return 0
    if w1>w2, return 1
    if w1<w2, return -1
    w1 is like 2016-08-01, w2 is like 08/01/16'''
    de = we.split("-")  #get different parts of the date data
    dw = ww.split("/")
    de = de[0]+de[1]+de[2]  #connect the different parts to be a string for comparison
    dw = "20" + dw[2]+dw[0] + dw[1]
    if dw == de:
        return 0
    elif dw>de:
        return 1
    else:
        return -1

def do_merging(e, w, re = sys.stdout):  
    '''e is the data of energy, w is the data of water
    try to find the nearest time of water to match it with energy,
    and print energy value behind it.
    fout is the filename to write in, if no filename given, output the STDOUT stream.
    '''
    n_energy = 0
    currentEnergyDay = e[0][0]
    for index in range(len(w)):
        re.write(",".join(str(x) for x in data_water[index]))
        re.write(",")

        if compareto(w[index][1].split()[0], currentEnergyDay)>=0:
            if (compareto(w[index][1].split()[0], currentEnergyDay))==1: raise Exception
            if n_energy<len(e):
                re.write(str(e[n_energy][1]/1000))
            n_energy+=1
            if n_energy<len(e):
                currentEnergyDay = e[n_energy][0]
        re.write("\n")

#read energy data and change the type of value to float
dataenergy = open(sys.argv[2])
data_energy = []
for i in dataenergy.readlines():
    data = i.strip().split(",")
    data[0] = data[0].split(" ")[0]
    if data != [""]:
        data_energy.append(data)
dataenergy.close()
data_energy = data_energy[1:-1]   #remove the lines that are of no use
for i in range(len(data_energy)):
    data_energy[i][1] = float(data_energy[i][1])

#read water data and change the type of # to int and value to float
datawater = open(sys.argv[1])
data_water = []
for i in datawater.readlines():
    data = i.strip().split(",")
    if data != [""]:
        data_water.append(data)

data_water = data_water[2:]   #remove the line that is of no use
for i in range(len(data_water)):
    data_water[i][0] = int(data_water[i][0])
    data_water[i][2] = float(data_water[i][2])
datawater.close()


#check if the file is sorted by time
check(data_energy)


#creat the output file
if len(sys.argv)==5:
    string = sys.argv[4]
    filename = open(sys.argv[3], string)
#print the names of each column as the first line
    filename.write(",".join(['"#"','"Date Time, GMT-05:00"','"K-Type, °F (LGR S/N: 10679014, SEN S/N: 10679014, LBL: water pipe)"','"Energy Produced (kWh)"']))
    filename.write("\n")
    do_merging(data_energy, data_water, filename)
    filename.close()
#if no filename for writing is given, print directly
elif len(sys.argv)==3:
    sys.stdout.write(",".join(['"#"','"Date Time, GMT-05:00"','"K-Type, °F (LGR S/N: 10679014, SEN S/N: 10679014, LBL: water pipe)"','"Energy Produced (kWh)"']))

    do_merging(data_energy, data_water) 
else:
    raise IOError("It can only take four or three arguments")
#do_merging(data_energy, data_water)
