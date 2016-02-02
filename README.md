# Consumer Driven Contracts using Mountebank
We want to test the integration between a provider and 3 consumers:
* A provider that stores records,
* A consumer that gets records and requires them to contain fields a and b,
* A consumer that gets records and requires them to contain fields b and c,
* A consumer that updates records via a PATCH request .

# Consumer Driven Contracts
The configuaration file for Mountebank's imposters contains most of the
detail of the consumer contracts.  In addition to this tests should use
assertions that follow Postel's law
(i.e. requests sent by consumers should match the contract exatly, responses sent
by producers can contain fields that weren't defined in the contract) (see
(https://github.com/realestate-com-au/pact/wiki/Matching-gotchas for more detail)

## Set up
* Clone the repository
* Install Mountebank (may need to change if you're running on a different OS),
```
cd consumer_contracts_for_provider
./bootsrap
```

## Test the provider against the contract
```
cd provider
./run_tests.sh
```
## References
* [Consumer-Driven Contracts: A Service Evolution Pattern](http://martinfowler.com/articles/consumerDrivenContracts.html)
* [Mountebank](http://www.mbtest.org)
* [Chatpter 7 of Building Microservices by Sam Newman](http://shop.oreilly.com/product/0636920033158.do)

# To do
* Add simple implementation of consumers with tests.
* Add overview of how changes to contracts, providers and consumers can
  be handled going forward.
