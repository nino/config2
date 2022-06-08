package clickup

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
	"strings"
)

func buildUrl(parts ...string) string {
	builder := strings.Builder{}
	for _, part := range parts {
		builder.WriteString(part)
	}
	return builder.String()
}

func getRequestWithToken(token, url string) ([]byte, error) {
	req, err := http.NewRequest(http.MethodGet, url, nil)
	if err != nil {
		log.Print("Failed to create a request")
		return []byte{}, err
	}

	req.Header.Set("Authorization", token)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Print("Failed to do the request")
		return []byte{}, err
	}
	defer resp.Body.Close()

	b, readErr := io.ReadAll(resp.Body)
	if readErr != nil {
		log.Print("something really went wrong here")
		return []byte{}, readErr
	}

	return b, nil
}

func GetUser(token string) (User, error) {
	log.Printf("Fetching user...")
	b, reqErr := getRequestWithToken(token, "https://api.clickup.com/api/v2/user")
	if reqErr != nil {
		return User{}, reqErr
	}

	var payload struct {
		TheUser User `json:"user"`
	}
	unmarshalErr := json.Unmarshal(b, &payload)
	if unmarshalErr != nil {
		log.Print("Invalid user received")
		return User{}, unmarshalErr
	}

	return payload.TheUser, nil
}

func GetTeams(token string) ([]Team, error) {
	log.Printf("Fetching teams...")
	b, reqErr := getRequestWithToken(token, "https://api.clickup.com/api/v2/team")
	if reqErr != nil {
		return []Team{}, reqErr
	}

	var payload struct {
		Teams []Team `json:"teams"`
	}
	unmarshalErr := json.Unmarshal(b, &payload)
	if unmarshalErr != nil {
		log.Print("Invalid user received")
		return []Team{}, unmarshalErr
	}

	return payload.Teams, nil
}

func GetSpaces(token string, teamId string) ([]Space, error) {
	log.Printf("Fetching spaces for team ID %s...", teamId)
	url := buildUrl("https://api.clickup.com/api/v2/team/", teamId, "/space")
	b, reqErr := getRequestWithToken(token, url)
	if reqErr != nil {
		return []Space{}, reqErr
	}

	var payload struct {
		Spaces []Space `json:"spaces"`
	}
	unmarshalErr := json.Unmarshal(b, &payload)
	if unmarshalErr != nil {
		log.Print("Invalid user received")
		return []Space{}, unmarshalErr
	}

	return payload.Spaces, nil
}

func GetFolders(token string, spaceId string) ([]Folder, error) {
	log.Printf("Fetching folders for space ID %s...", spaceId)
	url := buildUrl("https://api.clickup.com/api/v2/space/", spaceId, "/folder")
	b, reqErr := getRequestWithToken(token, url)
	if reqErr != nil {
		return []Folder{}, reqErr
	}

	var payload struct {
		Folders []Folder `json:"folders"`
	}
	unmarshalErr := json.Unmarshal(b, &payload)
	if unmarshalErr != nil {
		log.Print("Invalid user received")
		return []Folder{}, unmarshalErr
	}

	return payload.Folders, nil
}

func GetTasks(token string, listId string) ([]Task, error) {
	log.Printf("Fetching tasks for list ID %s...", listId)
	url := buildUrl("https://api.clickup.com/api/v2/list/", listId, "/task")
	b, reqErr := getRequestWithToken(token, url)
	if reqErr != nil {
		return []Task{}, reqErr
	}

	var payload struct {
		Tasks []Task `json:"tasks"`
	}
	unmarshalErr := json.Unmarshal(b, &payload)
	if unmarshalErr != nil {
		log.Print("Invalid user received")
		return []Task{}, unmarshalErr
	}

	return payload.Tasks, nil
}

func GetLists(token string, folderId string) ([]List, error) {
	log.Printf("Fetching lists for folder ID %s...", folderId)
	url := buildUrl("https://api.clickup.com/api/v2/folder/", folderId, "/list")
	b, reqErr := getRequestWithToken(token, url)
	if reqErr != nil {
		return []List{}, reqErr
	}

	var payload struct {
		Lists []List `json:"lists"`
	}
	unmarshalErr := json.Unmarshal(b, &payload)
	if unmarshalErr != nil {
		log.Print("Invalid user received")
		return []List{}, unmarshalErr
	}

	return payload.Lists, nil
}
