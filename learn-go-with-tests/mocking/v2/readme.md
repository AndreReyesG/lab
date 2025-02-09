# Test the operation order
`Countdown` should sleep before each next print.
In **v1** only asserts that it has slept three times, but those sleeps could occur out of sequence.

If we change the code of `Countdown` to the following:
```go
func Countdown(out io.Writer, sleeper Sleeper) {
	for i := countdownStart; i > 0; i-- {
		sleeper.Sleep()
	}

	for i := countdownStart; i > 0; i-- {
		fmt.Fprintln(out, i)
	}

	fmt.Fprint(out, finalWord)
}
```
The test should still passing even though the implementation is wrong.

We have **two different dependencies** and we want to record all of their operations into one list. So we created on *spy* for them both.

```go
type SpyCountdownOperations struct {
	Calls []string
}

func (s *SpyCountdownOperations) Sleep() {
	s.Calls = append(s.Calls, sleep)
}

func (s *SpyCountdownOperations) Write(p []byte) (n int, err error) {
	s.Calls = append(s.Calls, write)
	return
}

const write = "write"
const sleep = "sleep"
```
