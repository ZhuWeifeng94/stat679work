#This shell script is used to grep information from log file
echo name,h,Cputime > summary_zwf.csv    #add the first line as colnames
for filename in ./out/*.out
    do
	a=`grep 'time' $filename | grep -Eo "\d+\.\d+"`   #get the CPUtime
	b=`echo $filename | cut -d / -f 3 | cut -d . -f 1`   #get the name for analysis
	d=`cat ./log/$b\.log | grep 'hmax = ' $c | grep -o "\d"`   #get the value of hmax
	echo $b,$d,$a >> summary_zwf.csv   #write the values I need into the csv file
    done
