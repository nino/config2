package main

import (
	"fmt"
	cu "github.com/nino/config/projects/clickup/src"
	"log"
	"os"
	"strings"
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

func maybePanic(err error, msg string) {
	if err != nil {
		log.Fatal(err, msg)
	}
}

func main() {
	// var user cu.User

	// err := json.Unmarshal([]byte("{ \"username\": \"Nino\", \"dob\": 1234567890, \"color\": \"12121\" }"), &user)
	// if err != nil {
	// 	panic(err)
	// }
	// fmt.Printf("%+v\n", user)

	// bytes, marshalErr := json.Marshal(user)
	// if marshalErr != nil {
	// 	panic(marshalErr)
	// }

	// fmt.Printf("%s\n", string(bytes))

	// for i := 0; i < 100; i += 1 {
	// 	fuzzySearch("äbc", []string{"one", "two", "älphabetic", "aeeeexbeeeeaaaaccccc"})
	// }

	// fmt.Printf("%+v\n", fuzzySearch("äbc", []string{"one", "two", "älphabetic", "aeeeexbeeeeaaaaccccc"}))
	// fmt.Printf("%+v\n", string("äbßß"[0]))

	token := os.Getenv("CLICKUP_TOKEN")

	// user, err := cu.GetUser(token)
	// maybePanic(err, "Unable to get user")

	teams, getTeamsErr := cu.GetTeams(token)
	maybePanic(getTeamsErr, "Unable to get teams")

	if len(teams) < 1 {
		log.Fatal("No teams found")
	}
	immoTeam := teams[0]

	spaces, getSpacesErr := cu.GetSpaces(token, immoTeam.Id)
	maybePanic(getSpacesErr, "Unable to get spaces for team")

	prodSpace := cu.Space{}
	for _, space := range spaces {
		if space.Name == "Product" {
			prodSpace = space
		}
	}
	if prodSpace.Name == "" {
		log.Fatal("Product space not found")
	}

	tasks := []cu.Task{}

	log.Print("Space:", prodSpace)
	folders, getFoldersErr := cu.GetFolders(token, prodSpace.Id)
	maybePanic(getFoldersErr, "Unable to get folders")

	for _, folder := range folders {
		log.Printf("Will now fetch lists for folder %s...", folder.Name)
		lists, getListsErr := cu.GetLists(token, folder.Id)
		maybePanic(getListsErr, "Unable to get lists in folder")

		for _, list := range lists {
			nextTasks, getTasksErr := cu.GetTasks(token, list.Id)
			maybePanic(getTasksErr, "Unable to get tasks in list")
			tasks = append(tasks, nextTasks...)
		}
	}

	for _, task := range tasks {
		fmt.Println(task.Id, ", ", task.GetCustomFieldValue("Jira Issue Key"), ", ", task.CustomId)
	}
}
