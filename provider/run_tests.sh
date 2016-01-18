#!/usr/bin/env bash

set -e

cd ../mountebank
./start_mountebank &> /dev/null &
mountebank_pid=$!
sleep 1
echo "mountebank pid=$mountebank_pid"
cd -

cd provider
python -m SimpleHTTPServer 1912 &> /dev/null &
provider_pid=$!
sleep 1
echo "provider_pid=$provider_pid"
cd -

python test.py

kill "$provider_pid"

cd ../mountebank
./mb stop
cd -
