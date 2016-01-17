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
* Add code to predicate in consumer 3 so that it can handle the keys in the dictionary in any order (should take a look at "Predicate injection" and https://www.npmjs.com/package/deep-equal 
* Add a consumer, with tests that use the mountebank instance as stub
* Move contracts out of mountebank folder and into a separate one (I don't thing that these should be in the provider or consumer repo because don't want to have to checkout the providers whole repo if working on the consumer and vice versa.)
* What happens when predicates of one consumer are a subset of another consumer?
