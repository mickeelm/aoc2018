#!/bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
reset=`tput sgr0`
scriptdir="$(cd "$(dirname "$0")" && pwd)"

function run_test() {
  if [ $2 == "dummy" ]
  then 	  
    input_filename="test_input_$1"
    answer_filename="$scriptdir/test_answer_$1"
  else 
    input_filename="input"
    answer_filename="$scriptdir/real_answer_$1"
  fi

  if [ ! -s $answer_filename ]
  then
    echo -e "${yellow}Test $1 [$2] ignored (no answer set)${reset}"
    return 0
  fi

  result=`python $scriptdir/part$1.py $input_filename`
  answer=`head -n 1 $answer_filename` 

  if [ $result == $answer ] 
  then
    echo -e "${green}Test $1 [$2] passed${reset}"
  else
    echo -e "${red}Test $1 [$2] failed. Result was [${reset}$result${red}], expecting [${reset}$answer${red}]${reset}"
  fi
}

run_test 1 dummy
run_test 1 real
run_test 2 dummy
run_test 2 real
