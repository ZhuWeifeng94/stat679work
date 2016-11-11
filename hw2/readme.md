#escription of the repository
##Data
Here are two data files that used in hw2:
* [energy.csv]:(https://github.com/UWMadison-computingtools/coursedata/blob/master/hw2-datamerge/energy.csv)
 : daily data on the energy produced by a photovoltaic system
<p>Two kinds of infomation is shown here: 
 1. date for counting the energy data
 2. data of energy
- [waterTemperature.csv]:(https://github.com/UWMadison-computingtools/coursedata/blob/master/hw2-datamerge/waterTemperature.csv) 
 : hourly data on the hot water temperature
<p>Three kinds of infomation is shown here:
 1. #of the record
 2. time for taking the data
 3. water pipe value

##scripts
I put the script that I used for the homework here. Which is named [hw2.py]:(https://github.com/ZhuWeifeng94/stat679work/blob/master/hw2/scripts/hw2.py)
<p> This file can be run like this: **python hw2.py \<filename1\> \<filename2\> \<outputfile\> \<action\>**
<p> or **python hw2.py \<filename1\> \<filename2\>**
* here, filename1 = waterTemperature.csv
- filename2 = energy.csv
- outputfile = the name that you want for the outputfile
- action can be a or w, "a" means you want to append the result to the output file, "w" mean you want to overwrite the file
- **if you use the the second style with only two file names, then it will return the output to the STDOUT stream.**

<p> This homework is asked to combine two files to one, which contains more infomation.
And the constrain is 
> The energy value for a particular time should be matched with (placed on the same row as) the temperature data logged just before that time.

##results
Here result.csv is the file that I returned. 
