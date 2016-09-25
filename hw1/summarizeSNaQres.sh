touch summary_zwf.csv
for filename in ./out/*.out
    do
	a=`grep 'time' $filename | cut -d ' ' -f 4`
	b=`echo $filename | cut -d / -f 3 | cut -d . -f 1`
        c=`echo ./log/$b\.log`
	d=`grep 'hmax' $c | head -1 | cut -d ' ' -f 4 | cut -d , -f 1`
	echo $b $d $a >> summary_zwf.csv
    done
