.PHONY: directories clean ui exe

all:

ui: ui/mainui.ui
	pyuic5 ./ui/mainui.ui -o ./ui/mainwindow.py

exe: nukl_enroll_client.py ui/mainwindow.py
	pyinstaller -F -w ./nukl_enroll_client.py

clean:
	rm -rf dist build __pycache__
stat:
	wc src/*
