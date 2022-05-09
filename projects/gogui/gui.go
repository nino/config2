package main

import (
	"github.com/diamondburned/gotk4/pkg/gdk/v4"
	"github.com/diamondburned/gotk4/pkg/gtk/v4"
	"log"
	"os"
)

var todos []string = []string{"One", "Two"}
var todosBox *gtk.Box
var globalWin *gtk.Window

const (
	MOD_NOTHING = uint(0)
	MOD_SHIFT   = uint(gdk.SHIFT_MASK)
	MOD_CTRL    = uint(gdk.CONTROL_MASK)
	MOD_OPTION  = uint(gdk.MOD1_MASK)
	MOD_COMMAND = uint(gdk.MOD2_MASK)
)

// KeyVal values
const (
	KEY_RETURN = 65293
)

func isKeyCombo(event *gdk.Event, modMasks uint, keyVal uint) bool {
	keyEvent := &gdk.EventKey{Event: event}
	state := keyEvent.State() & (MOD_NOTHING | MOD_CTRL | MOD_COMMAND | MOD_OPTION | MOD_SHIFT)
	return (state == modMasks) && keyEvent.KeyVal() == keyVal
}

func maybeFail(msg string, err error) {
	if err != nil {
		log.Fatal(msg, err)
	}
}

func todoItem(text string) *gtk.Box {
	label, labelErr := gtk.NewLabel(text)
	maybeFail("Unable to create label: ", labelErr)
	button, buttonErr := gtk.NewButtonWithLabel("×") // This is very bad
	maybeFail("Unable to create button: ", buttonErr)

	layout, err := gtk.NewBox(gtk.OrientationHorizontal, 8)
	maybeFail("Unable to create layout for todo item: ", err)

	layout.Add(button)
	layout.Add(label)
	return layout
}

func initTodoList() {
	layout, boxErr := gtk.NewBox(gtk.OrientationVertical, 8)
	if boxErr != nil {
		log.Fatal("Unable to create stack", boxErr)
	}

	for _, t := range todos {
		label := todoItem(t)
		layout.Add(label)
	}

	todosBox = layout
}

func addTodo(text string) {
	log.Print("Adding TODO", text)
	widget := todoItem(text)
	todosBox.Add(widget)
	todosBox.CheckResize()
	log.Print(todosBox.GetChildren().Length())
	todosBox.GetChildren().Foreach(func(child interface{}) {
		log.Print("Child: ", child)
	})
	todosBox.ShowAll()
}

var newTodoForm *gtk.Box

func initNewTodoForm() {
	layout, boxErr := gtk.NewBox(gtk.ORIENTATION_HORIZONTAL, 8)
	if boxErr != nil {
		log.Fatal("Unable to create box for new todo form:", boxErr)
	}

	textField, textFieldErr := gtk.EntryNew()
	if textFieldErr != nil {
		log.Fatal("Unable to create text view:", textFieldErr)
	}
	layout.Add(textField)

	addButton, buttonErr := gtk.NewButtonWithLabel("Add")
	if buttonErr != nil {
		log.Fatal("Unable to add button:", buttonErr)
	}

	doAddTodo := func() {
		text, _ := textField.GetText()
		addTodo(text)
		textField.SetText("")
	}

	addButton.Connect("clicked", doAddTodo)
	layout.Add(addButton)

	textField.Connect("key-press-event", func(field *gtk.Entry, event *gdk.Event) {
		if isKeyCombo(event, MOD_NOTHING, KEY_RETURN) {
			doAddTodo()
		}
	})

	newTodoForm = layout
}

func mainContainer() *gtk.Box {
	layout, boxErr := gtk.NewBox(gtk.OrientationVertical, 8)
	if boxErr != nil {
		log.Fatal("Unable to create main container:", boxErr)
	}

	initTodoList()
	layout.Add(todosBox)

	initNewTodoForm()
	layout.Add(newTodoForm)

	layout.SetBorderWidth(8)
	return layout
}

func setUpOpeningFiles(app *gtk.Application) {
	log.Print(app)
}

func main() {
	app := gtk.NewApplication("com.ninoan.gtk4-app", 0)

	win, err := gtk.NewWindow()
	if err != nil {
		log.Fatal("Unable to create window:", err)
	}
	win.SetTitle("TodoMVC")
	win.Connect("destroy", func() {
		gtk.MainQuit()
	})
	win.Connect("key-press-event", func(win *gtk.Window, event *gdk.Event) {
		if isKeyCombo(event, MOD_COMMAND, 'w') {
			win.Close()
		}
	})

	globalWin = win
	mainLayout := mainContainer()
	win.Add(mainLayout)

	// Recursively show all widgets contained in this window.
	win.ShowAll()
	gtk.Main()
}
