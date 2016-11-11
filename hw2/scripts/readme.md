#scripts
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

The algorithm is given by the professor, which is in data/. 
