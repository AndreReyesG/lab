package main

import (
	"os"
	"testing"
)

func createTempFile(t testing.TB, initialData string) (*os.File, func()) {
	t.Helper()

	tmpfile, err := os.CreateTemp("", "db")

	if err != nil {
		t.Fatalf("could not create temp file %v", err)
	}

	tmpfile.Write([]byte(initialData))

	removeFile := func() {
		tmpfile.Close()
		os.Remove(tmpfile.Name())
	}

	return tmpfile, removeFile
}

func TestFileSystemStore(t *testing.T) {
	t.Run("league from reader", func(t *testing.T) {
		database, cleanDatabase := createTempFile(t, `[
            {"Name": "Moka", "Wins": 10},
            {"Name": "Milky", "Wins": 20}]`)
		defer cleanDatabase()

		store, err := NewFileSystemPlayerStore(database)
		assertNoError(t, err)

		got := store.GetLeague()

		want := League{
			{"Milky", 20},
			{"Moka", 10},
		}

		assertLeague(t, got, want)

		// read again
		got = store.GetLeague()
		assertLeague(t, got, want)
	})

	t.Run("get player score", func(t *testing.T) {
		database, cleanDatabase := createTempFile(t, `[
            {"Name": "Moka", "Wins": 10},
            {"Name": "Milky", "Wins": 20}]`)
		defer cleanDatabase()

		store, err := NewFileSystemPlayerStore(database)
		assertNoError(t, err)

		got := store.GetPlayerScore("Moka")
		want := 10
		assertScoreEquals(t, got, want)
	})

	t.Run("store wins for existing players", func(t *testing.T) {
		database, cleanDatabase := createTempFile(t, `[
            {"Name": "Moka", "Wins": 10},
            {"Name": "Milky", "Wins": 20}]`)
		defer cleanDatabase()

		store, err := NewFileSystemPlayerStore(database)
		assertNoError(t, err)

		store.RecordWin("Moka")

		got := store.GetPlayerScore("Moka")
		want := 11
		assertScoreEquals(t, got, want)
	})

	t.Run("store wins for new players", func(t *testing.T) {
		database, cleanDatabase := createTempFile(t, `[
            {"Name": "Moka", "Wins": 10},
            {"Name": "Milky", "Wins": 20}]`)
		defer cleanDatabase()

		store, err := NewFileSystemPlayerStore(database)
		assertNoError(t, err)

		store.RecordWin("Ana")

		got := store.GetPlayerScore("Ana")
		want := 1
		assertScoreEquals(t, got, want)
	})
}

func assertScoreEquals(t testing.TB, got, want int) {
	t.Helper()
	if got != want {
		t.Errorf("got %d want %d", got, want)
	}
}

func assertNoError(t testing.TB, err error) {
	t.Helper()
	if err != nil {
		t.Fatalf("didn't expect an error but got one, %v", err)
	}
}
