# Mocking
> [!NOTE]
> Check <a href="https://martinfowler.com/bliki/TestDouble.html">Martin Flower's Test Double post</a>.
> Check [Martin Flower's Test Double post](https://martinfowler.com/bliki/TestDouble.html).

We have a dependency on `Sleep`ing which we need to extract so we can then control it in our tests.

If we can *mock* `time.Sleep` we can use *dependency injection* to use it instead of a "real" `time.Sleep` and the we can **spy on the calls** to make assertions on them.

We define our dependency as an interface (`Sleeper`). This lets us then use a *real* Sleeper (`DefaultSleeper`) in `main` and a *spy spleeper* (`SpySleeper`) in our test.
