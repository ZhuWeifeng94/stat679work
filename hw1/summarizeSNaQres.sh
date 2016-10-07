#This is the script for hw2, to get infomation from the log file.
echo name,h,Cputime,Nruns,Nfail,fabs,frel,xabs,xrel,seed,under3460,under3450,under3440 > summary_zwf.csv 
for filename in ./out/*.out
    do
#These are for exercise 2
	a=`grep 'time' $filename | grep -Eo "\d+\.\d+"`   #get the CPUtime
	b=`basename -s ".out" $filename`    #get the name for analysis
        c=`echo ./log/${b}.log`   #save the name for file to use
	d=`cat ./log/$b\.log | grep 'hmax = ' $c | grep -o "\d"`   #get the value of hmax

	e=`grep runs $c | sed -E -n 's/.* ([0-9]+) runs.*/\1/p'` #get number of runs

	f=`grep proposals $c  | sed -E -n 's/.*proposals = ([0-9]+).*/\1/p'` #get max number of fails

    	g=`grep ftolAbs $c | sed -E -n 's/.*ftolRel=([0-9.e-]+).*=([0-9.e-]+).*/\2 \1/p'` #get ftoAbs and ftoRel

    	h=`grep xtolAbs $c | sed -E -n 's/.*xtolAbs=([0-9.e-]+).*=([0-9.e-]+).*/\2 \1/p'` #get xAbs and xRel

	i=`grep seed $c | sed -E -n 's/main seed ([0-9]+).*/\1/p'` #get seeds value

	j=`grep loglik $c | sed -E -n 's/.* of best ([0-9]+)..*/\1/p'` #get values of runs
	k1=0
	k2=0
	k3=0
	for s in $j
	    do
		if [ $s -lt 3460 ]
		then 
		    k1=$((k1+1))   #count the number of values lower than 3460
		fi
		if [ $s -lt 3450 ]
		    then k2=$((k2+1))   #count the number of values lower than 3460
		fi
		if [ $s -lt 3440 ]
		    then k3=$((k3+1))   #count the number of values lower than 3460
		fi
	    done
#put all these values I get to a csv.
	echo $b,$d,$a,$e,$f,$g,$h,$i,$k1,$k2,$k3 >> summary_zwf.csv
    done
