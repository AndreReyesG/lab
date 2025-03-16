package main

import (
	"strings"
	"testing"
)

func TestFileSystemStore(t *testing.T) {
	t.Run("league from reader", func(t *testing.T) {
		database := strings.NewReader(`[
            {"Name": "Moka", "Wins": 10},
            {"Name": "Milky", "Wins": 20}]`)

		store := FileSystemPlayerStore{database}
		got := store.GetLeague()

		want := []Player{
			{"Moka", 10},
			{"Milky", 20},
		}

		assertLeague(t, got, want)
	})
}
