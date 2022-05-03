run:
	go run gui.go

app:
	go build -ldflags "-s -w" gui.go
	mkdir -p GUI.app/Contents/MacOS
	cp Info.plist GUI.app/Contents
	cp gui GUI.app/Contents/MacOS
