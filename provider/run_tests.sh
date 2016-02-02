#!/usr/bin/env bash

set -e
set -x

export CONSUMER_CONTRACTS_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )/../consumer_contracts_for_provider" && pwd )"
cd "$CONSUMER_CONTRACTS_ROOT"
./restart_mountebank &> /dev/null &
mountebank_pid=$!
sleep 2
echo "mountebank pid=$mountebank_pid"
cd -

python provider.py &> /dev/null &
provider_pid=$!
sleep 2
echo "provider_pid=$provider_pid"

python test.py

kill "$provider_pid"

cd ../consumer_contracts_for_provider
./mb stop
cd -
