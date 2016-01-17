# Consumer Driven Contracts using Mountebank
## Set up
* Clone the repository
* run ./bootsrap to install Mountebank (you may need to to change the version you install depending on your os)

## Test the provieder against the contract
* cd provider
* ./run_tests.sh

## References
* http://www.mbtest.org

# To do
* Add a consumer, with tests that use the mountebank instance as stub
* Add a json document in predicate example
* Move contracts out of mountebank folder and into a separate one (I don't thing that these should be in the provider or consumer repo because don't want to have to checkout the providers whole repo if working on the consumer and vice versa.)
