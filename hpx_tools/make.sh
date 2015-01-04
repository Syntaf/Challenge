#!/bin/bash
# This is a very useful linux script for building anything HPX on the
# Hermione cluster. Made by Martin Stumpf

SCRIPTPATH=$( cd $(dirname $0) ; pwd -P )
INSTALL_PATH=$SCRIPTPATH/install
BUILD_PATH=$SCRIPTPATH/build

if [ "$1" = "clean" ]; then
		rm -rf $INSTALL_PATH $BUILD_PATH
		exit 0
fi

export CC=/usr/bin/gcc
export CXX=/usr/bin/g++

if [ ! -d "$BUILD_PATH" ]; then
		mkdir -p "$BUILD_PATH"

		cd "$BUILD_PATH"

		cmake -DHPX_NO_INSTALL=On				\
			  -DBOOST_ROOT=$HOME/boost/install	\
			  -DCMAKE_BUILD_TYPE=Release		\
			  -DHPX_HAVE_PARCELPORT_MPI=True	\
			  -DHPX_MALLOC="jemalloc"			\
			  -DCMAKE_CXX_FLAGS="-w"			\
			  -Wdev								\
			  $SCRIPTPATH/repo
fi

cd "$BUILD_PATH"

make $1 -k -j
