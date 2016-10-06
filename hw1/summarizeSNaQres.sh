touch summary_zwf.csv
for filename in ./out/*.out
    do
#These are for exercise 2
	a=`grep 'time' $filename | cut -d ' ' -f 4`
	b=`basename -s ".out" $filename`
        c=`echo ./log/$b\.log`
	d=`grep 'hmax' $c | head -1 | cut -d ' ' -f 4 | cut -d , -f 1`
#get number of runs
	e=`grep runs $c | sed -E -n 's/.* ([0-9]+) runs.*/\1/p'`
#get max number of fails
	f=`grep proposals $c  | sed -E -n 's/.*proposals = ([0-9]+).*/\1/p'`
#get ftoAbs and ftoRel
    	g=`grep ftolAbs $c | sed -E -n 's/.*ftolRel=([0-9.e-]+).*=([0-9.e-]+).*/\2 \1/p'`
#get xAbs and xRel
    	h=`grep xtolAbs $c | sed -E -n 's/.*xtolAbs=([0-9.e-]+).*=([0-9.e-]+).*/\2 \1/p'`
#get seeds value
	i=`grep seed $c | sed -E -n 's/main seed ([0-9]+).*/\1/p'`
#get values of runs
	j=`grep loglik $c | sed -E -n 's/.* of best ([0-9]+)..*/\1/p'`
	k1=0
	k2=0
	k3=0
	for s in $j
	    do
		if [ $s -lt 3460 ]
		then 
		    k1=$((k1+1))
		fi
		if [ $s -lt 3450 ]
		    then k2=$((k2+1))
		fi
		if [ $s -lt 3440 ]
		    then k3=$((k3+1))
		fi
	    done
#put all these values I get to a csv.
	echo $b $d $a $d $e $f $g $h $i $k1 $k2 $k3 >> summary_zwf.csv
    done
