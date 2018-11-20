#!/usr/bin/env bash


#Slide 1: test cases with brute force correct answers
#Slide 2: pseudocode of implementation
#Slide 3: Validating correctness as test cases via small n=1,2,3...10
#Slide 4: validating performance via large n=1,2,3,......1000



#generate test cases
python test_cases.py

#generate correct answers for 10 test cases with brute force
python run.py