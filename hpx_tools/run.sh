#!/bin/bash


APP="$@"
APP="$APP -Ihpx.parcel.tcp.enable=0"
APP="$APP -Ihpx.parcel.bootstrap=mpi"
APP="$APP -Ihpx.parcel.mpi.max_connections=65536"
APP="$APP -Ihpx.parcel.mpi.max_connections_per_locality=2048"
APP="$APP -Ihpx.parcel.mpi.use_io_pool=1"
APP="$APP -Ihpx.stacks.use_guard_pages=0"
APP="$APP -Ihpx.stacks.large_size=0x800000"
APP="$APP -Ihpx.stacks.medium_size=0x80000"
APP="$APP -Ihpx.stacks.small_size=0x20000"



threads=16
srun -p marvin -N 1 $APP -t$threads
#$APP -t$threads
