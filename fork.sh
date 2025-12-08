#!/bin/bash

echo "Parent PID: $$"   # $$ gives PID of current script

# Creating child process 1
(sleep 2; echo "Child 1 finished with PID: $!") &
pid1=$!

# Creating child process 2
(sleep 3; echo "Child 2 finished with PID: $!") &
pid2=$!

echo "Child 1 PID: $pid1"
echo "Child 2 PID: $pid2"

wait $pid1
wait $pid2
echo "Both Child Processes Completed."