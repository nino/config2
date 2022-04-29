package main

import (
	"encoding/json"
	"fmt"
	cu "github.com/nino/config/projects/clickup/src"
	"strings"
	"os"
)

func isFuzzyMatch(query []rune, potentialCandidate string) bool {
	if len(query) == 0 {
		return true
	}

	firstIndex := strings.IndexRune(potentialCandidate, query[0])
	if firstIndex == -1 {
		return false
	}

	return isFuzzyMatch(query[1:], potentialCandidate[firstIndex:])
}

func fuzzySearch(needle string, haystack []string) []string {
	runes := []rune(needle)
	res := make([]string, 0, len(haystack))
	for _, bitOfHay := range haystack {
		if isFuzzyMatch(runes, bitOfHay) {
			res = append(res, bitOfHay)
		}
	}
	return res
}

func main() {
	var user cu.User

	err := json.Unmarshal([]byte("{ \"username\": \"Nino\", \"dob\": 1234567890, \"color\": \"12121\" }"), &user)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%+v\n", user)

	bytes, marshalErr := json.Marshal(user)
	if marshalErr != nil {
		panic(marshalErr)
	}

	fmt.Printf("%s\n", string(bytes))

	for i := 0; i < 100; i += 1 {
		fuzzySearch("äbc", []string{"one", "two", "älphabetic", "aeeeexbeeeeaaaaccccc"})
	}

	fmt.Printf("%+v\n", fuzzySearch("äbc", []string{"one", "two", "älphabetic", "aeeeexbeeeeaaaaccccc"}))
	fmt.Printf("%+v\n", string("äbßß"[0]))


	token := os.Getenv("CLICKUP_TOKEN")
	u, e := cu.GetUser(token)
	if e != nil {
		panic(e)
	}

	fmt.Printf("User: %+v\n", u)
}
