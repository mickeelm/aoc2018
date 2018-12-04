mkdir $1
ln -s ../test.sh $1/test.sh

echo import sys > $1/part1.py
echo import os >> $1/part1.py
echo >> $1/part1.py
echo "inputfile=os.path.join(sys.path[0],sys.argv[1])" >> $1/part1.py
cp $1/part1.py $1/part2.py

touch $1/input
touch $1/real_answer_1
touch $1/real_answer_2
touch $1/test_input_1
touch $1/test_input_2
touch $1/test_answer_1
touch $1/test_answer_2
