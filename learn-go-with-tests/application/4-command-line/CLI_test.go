package poker_test

import (
	"github.com/AndreReyesG/lab/application/4-command-line"
	"strings"
	"testing"
)

func TestCLI(t *testing.T) {
	t.Run("record moka wins from user input", func(t *testing.T) {
		in := strings.NewReader("Moka wins\n")
		playerStore := &poker.StubPlayerStore{}

		cli := poker.NewCLI(playerStore, in)
		cli.PlayPoker()

		poker.AssertPlayerWin(t, playerStore, "Moka")
	})

	t.Run("record milky wins from user input", func(t *testing.T) {
		in := strings.NewReader("Milky wins\n")
		playerStore := &poker.StubPlayerStore{}

		cli := poker.NewCLI(playerStore, in)
		cli.PlayPoker()

		poker.AssertPlayerWin(t, playerStore, "Milky")
	})
}
