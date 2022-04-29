package clickup

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
)

func GetUser(token string) (User, error) {
	req, err := http.NewRequest(http.MethodGet, "https://api.clickup.com/api/v2/user", nil)
	if err != nil {
		log.Print("Failed to create a request")
		return User{}, err
	}

	req.Header.Set("Authorization", token)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Print("Failed to do the request")
		return User{}, err
	}
	defer resp.Body.Close()

	b, readErr := io.ReadAll(resp.Body)
	if readErr != nil {
		log.Print("something really went wrong here")
		return User{}, readErr
	}
	log.Print(string(b))

	var payload struct {
		TheUser User `json:"user"`
	}
	err2 := json.Unmarshal(b, &payload)
	if err2 != nil {
		log.Print("Invalid user received")
		return User{}, err
	}

	return payload.TheUser, nil
}
