#!/bin/bash

NUM_MACHINES=1

srun -p marvin -t 02:00:00 -n$NUM_MACHINES -N$NUM_MACHINES --pty "$@"
