# Consumer Driven Contracts using Mountebank
We want to test the integration between a provider and 3 consumers:
* A provider that stores records,
* A consumer that gets records and requires them to contain fields a and b,
* A consumer that gets records and requires them to contain fields b and c,
* A consumer that updates records via a POST request .

## Set up
* Clone the repository
* Install Mountebank (may need to change if you're running on a different OS),
```
cd consumer_contracts_for_provider
./bootsrap
```

## Test the provieder against the contract
```
cd provider
./run_tests.sh
```
## References
* http://www.mbtest.org

# To do
* Add simple implementation of provider and consumers.
* Add references to Consumer Driven Contract resources.
* Add overview of how changes to contracts, providers and consumers can
  be handled going forward.
* Extract hard coded port numbers.
