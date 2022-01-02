#!/bin/bash

##
# make_test.sh
##

clear
TEST_DIR="./testfiles"
LS=`ls $TEST_DIR`

for FILE_NAME in $LS
do
	TEST_FILE="$TEST_DIR/$FILE_NAME"
	echo "./boj < $TEST_FILE"
	./boj < $TEST_FILE
done
