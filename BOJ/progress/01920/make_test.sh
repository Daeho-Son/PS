#!/bin/bash

##
# make_test.sh
##

TEST_DIR="./testfiles"
clear
LS=`ls $TEST_DIR`
for FILE_NAME in $LS
do
	TEST_FILE="$TEST_DIR/$FILE_NAME"
	echo "./boj < $TEST_FILE"
	./boj < $TEST_FILE
done
