#! /bin/bash
# ren.sh
#
#
# Simpleminded filename "rename" utility (based on "lowercase.sh")
# 

ARGS=2
E_BADARGS=85
ONE=1	#--------------------------------------------------------# For getting sigular/plural right (see below)

if [ $# -ne "$ARGS" ]
then
	echo "Usage: `basename $0` old-pattern new-pattern"
	## As in "ren gif jpg", renames all gif files in wdir to jpg ##
	exit $E_BADARGS
fi
number=0	#-----------------------------------------------# Keep track of how many files renamed :P

for filename in *$1*	#---------------------------------------# Traverse all matching files in dir
do
	if [ -f "$filename" ]	#-------------------------------# If finds match...
	then
		fname=`basename $filename`	#---------------# Strip off path
		n=`echo $fname | sed -e "s/$1/$2/"`	#-------# Substitute new for old in filename
		mv $fname $n	#-------------------------------# Renameee
		let "number += 1"
	fi
done

if [ "$number" -eq "$ONE" ]	#------------------------------# For correct grammar 
then
	echo "$number file renamed."
else
	echo "$number files renamed."
fi

exit $?
