#!/bin/bash

# Define the user inputs
input1="1"
input2="valves013,valves014"
input3="3"
input4="pipes008"
input5="pipes009"
input6="5"



# Run the Python program and pass the inputs
echo -e "$input1\n$input2\n$input3\n$input4\n$input5\n$input6" | python3 driver.py
