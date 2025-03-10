package main

import (
    "net/http/httptest"
    "net/http"
    "testing"
)

func TestGETPlayers(t* testing.T) {
    t.Run("returns Milky's score", func(t* testing.T) {
        request, _ := http.NewRequest(http.MethodGet, "/players/Milky", nil)
        response := httptest.NewRecorder()

        PlayerServer(response, request)

        got := response.Body.String()
        want := "20"

        if got != want {
            t.Errorf("got %q, want %q", got, want)
        }
    })
}
