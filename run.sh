#!/usr/bin/env bash


#generate test cases
python test_cases.py

#generate correct answers for 10 test cases with brute force
python run.py

#plot graph for validation of performance
python plot.py