package main

import (
	"github.com/diamondburned/gotk4/pkg/gtk/v4"
	"testing"
)

func TestFormatNumberWorks(t *testing.T) {
	if formatNumber(2) != "2" {
		t.Errorf("Positive numbers are broken")
	}

	if formatNumber(-2) != "–2" {
		t.Errorf("Negative numbers are broken")
	}
}

func TestIncrement(t *testing.T) {
	app := gtk.NewApplication("com.ninoan.todo-test_test", 0)
	t.Log("Running app…")
	app.ConnectActivate(func() {
		t.Log("Creating cmoponent")
		_ = NewCounterComponent(1)
		t.Log("Component created")
		app.Quit()
	})
	app.Run([]string{})
}
