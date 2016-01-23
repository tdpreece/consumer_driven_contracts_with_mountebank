#!/usr/bin/env bash

set -e

cd ../consumer_contracts_for_provider
./restart_mountebank &> /dev/null &
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

cd ../consumer_contracts_for_provider
./mb stop
cd -
