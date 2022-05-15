package main

import (
	"github.com/diamondburned/gotk4/pkg/gtk/v4"
	"log"
	"os"
	"strconv"
	"strings"
)

// KeyVal values
const (
	KEY_RETURN = 65293
)

func formatNumber(num int) string {
	return strings.ReplaceAll(strconv.Itoa(num), "-", "–")
}

func maybeFail(msg string, err error) {
	if err != nil {
		log.Fatal(msg, err)
	}
}

type CounterComponent struct {
	Widget *gtk.Box
	Value  int

	display *gtk.Label
}

func (counter *CounterComponent) Increment() {
	counter.Value += 1
	counter.display.SetText(formatNumber(counter.Value))
}

func (counter *CounterComponent) Decrement() {
	counter.Value -= 1
	counter.display.SetText(formatNumber(counter.Value))
}

func NewCounterComponent(initialValue int) CounterComponent {
	box := gtk.NewBox(gtk.OrientationVertical, 4)
	box.SetMarginTop(8)
	box.SetMarginBottom(8)
	box.SetMarginStart(8)
	box.SetMarginEnd(8)
	box.SetHExpand(true)
	box.SetVExpand(true)

	display := gtk.NewLabel(formatNumber(initialValue))
	display.SetHExpand(true)
	display.SetVExpand(true)
	display.SetVAlign(gtk.AlignCenter)

	buttonBox := gtk.NewBox(gtk.OrientationHorizontal, 4)
	buttonBox.SetHExpand(true)
	buttonBox.SetVExpand(false)
	buttonBox.SetHAlign(gtk.AlignCenter)

	plusButton := gtk.NewButtonWithLabel("+")
	plusButton.SetSizeRequest(16, 16)
	minusButton := gtk.NewButtonWithLabel("–")
	buttonBox.Append(plusButton)
	buttonBox.Append(minusButton)

	box.Append(display)
	box.Append(buttonBox)

	component := CounterComponent{
		Value:   initialValue,
		Widget:  box,
		display: display,
	}

	plusButton.ConnectClicked(func() { component.Increment() })
	minusButton.ConnectClicked(func() { component.Decrement() })

	return component
}

func main() {
	app := gtk.NewApplication("com.ninoan.todo-test", 0)
	app.ConnectActivate(func() { activate(app) })

	statusCode := app.Run(os.Args)
	if statusCode > 0 {
		os.Exit(statusCode)
	}
}

func activate(app *gtk.Application) {
	box := gtk.NewBox(gtk.OrientationVertical, 4)
	box.Append(NewCounterComponent(2).Widget)

	mainWindow := gtk.NewApplicationWindow(app)
	mainWindow.SetTitle("Counter App")
	mainWindow.SetChild(box)
	mainWindow.Show()
}
