package main

import (
    "fmt"
	"github.com/AndreReyesG/lab/application/4-command-line"
	"log"
	"os"
)

const dbFileName = "game.db.json"

func main() {
    store, close, err := poker.FileSystemPlayerStoreFromFile(dbFileName)

    if err != nil {
        log.Fatal(err)
    }
    defer close()

    fmt.Println("Let's play poker")
    fmt.Println("Type {Name} wins to record a win")
    poker.NewCLI(store, os.Stdin).PlayPoker()
}
