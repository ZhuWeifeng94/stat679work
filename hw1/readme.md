**Here are the shell scripts for hw1.**

**And for the 3rd question, I will return a csv file called [*summary_zwf.csv*](https://github.com/ZhuWeifeng94/stat679work/blob/master/hw1/summary_zwf.csv).**

#About data
<p>Two repositories are used named out and log.
<p>In log/, files are all named as <name>.log
<p>In out/, files are all named as <name>.log


#About scripts
##*In ex1*
I need to change the file names in out/.  
I use for loop and `mv` to change the name of out and log file.  
And the name for shell scripts is normalizeFileNames.sh.  
script: [normalizeFileNames.sh](https://github.com/ZhuWeifeng94/stat679work/blob/master/hw1/normalizeFileNames.sh)

##*In ex2*
I need to use `grep` function to get information from log files by for loop.  
And followed the professors suggestions, I rewrite the shell file into summarizeSNaQres_ex2.sh  
The information I need to find:  
* "analysis": the file name root
- "h": number after hmax
- "CPUtime": number after "Elapsed time"  
script: [summarizeSNaQres_ex2.sh](https://github.com/ZhuWeifeng94/stat679work/blob/master/hw1/summarizeSNaQres_ex2.sh)

##*In ex3*
I need to 
* use `sed` to get mroe information in log files.   
- use `basename` to get the name root but not grep
- use `if` to get what I need
- the information I need:
  0. The colmumns in ex2
  1. Nruns: number of runs
  2. Nfail:"max number of failed proposals"
  3. fabs: "ftolAbs"
  4. frel: "ftolRel"
  5. xabs: "xtolAbs"
  6. xrel: "xtolRel"
  7. seed: main seed
  8. under3460:  number of runs with a network score under 3460
  9. under3450: number of runs with a network score under 3450
  10. under3440: number of runs with a network score under 3440  
script: [summarizeSNaQres.sh](https://github.com/ZhuWeifeng94/stat679work/blob/master/hw1/summarizeSNaQres.sh)
