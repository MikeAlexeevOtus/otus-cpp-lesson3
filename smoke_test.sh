#!/bin/bash

set -eu
set -o pipefail

exe=$1

DATA_FILE=ip_filter.tsv
REFERENCE_VALUE=24e7a7b2270daee89c64d3ca5fb3da1a

echo testing with "$(which "$exe")"

md5=$($exe < $DATA_FILE | md5sum | cut -d' ' -f1)

test "$md5" == "$REFERENCE_VALUE"

echo OK
