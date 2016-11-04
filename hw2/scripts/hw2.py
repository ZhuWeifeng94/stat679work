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

def do_merging(e, w):  #e is the data of energy, w is the data of water
    n_energy = 0
    currentEnergyDay = e[0][0]
    for index in range(len(w)):
        print(",".join(str(x) for x in data_water_print[index]), end="")

        if compareto(w[index][1], currentEnergyDay)>=0:
            if (compareto(w[index][1], currentEnergyDay))==1: raise Exception
            if n_energy<len(e):
                print(",",e[n_energy][1]/1000, end="",sep = "")
            n_energy+=1
            if n_energy<len(e):
                currentEnergyDay = e[n_energy][0]
        print()

dataenergy = open("energy.csv")
data_energy = []
for i in dataenergy.readlines():
    data = i.strip().split(",")
    data[0] = data[0].split(" ")[0]
    if data != [""]:
        data_energy.append(data)
dataenergy.close()

data_energy = data_energy[1:-1]
for i in range(len(data_energy)):
    data_energy[i][1] = float(data_energy[i][1])


datawater = open("waterTemperature.csv")
data_water = []
for i in datawater.readlines():
    data = i.strip().split(",")
    if data != [""]:
        data_water.append(data)

data_water = data_water[2:]
for i in range(len(data_water)):
    data_water[i][0] = int(data_water[i][0])
    data_water[i][2] = float(data_water[i][2])
    data_water[i][1] = data_water[i][1].split()[0]
datawater.close()

datawater = open("waterTemperature.csv")
data_water_print = []
for i in datawater.readlines():
    data = i.strip().split(",")
    if data != [""]:
        data_water_print.append(data)
datawater.close()
data_water_print = data_water_print[2:]

print("#","Date Time, GMT-05:00","K-Type, °F (LGR S/N: 10679014, SEN S/N: 10679014, LBL: water pipe)","Energy Produced (kWh)", sep = ",")
do_merging(data_energy, data_water)
