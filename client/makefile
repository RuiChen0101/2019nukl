.PHONY: directories clean ui exe

all:

ui: src/ui/mainui.ui src/ui/ArrangementDialog.ui src/ui/MatchFinishDialog.ui src/ui/NewMatchDialog.ui src/ui/SetReplayDialog.ui src/ui/JudgeAssignDialog.ui
	pyuic5 ./src/ui/mainui.ui -o ./src/ui/mainwindow.py
	pyuic5 ./src/ui/ArrangementDialog.ui -o ./src/ui/ArrangementDialog.py
	pyuic5 ./src/ui/MatchFinishDialog.ui -o ./src/ui/MatchFinishDialog.py
	pyuic5 ./src/ui/NewMatchDialog.ui -o ./src/ui/NewMatchDialog.py
	pyuic5 ./src/ui/SetReplayDialog.ui -o ./src/ui/SetReplayDialog.py
	pyuic5 ./src/ui/JudgeAssignDialog.ui -o ./src/ui/JudgeAssignDialog.py

exe: nukl_enroll_client.py ui/mainwindow.py
	pyinstaller -F -w ./nukl_enroll_client.py

clean:
	rm -rf dist build __pycache__
stat:
	wc src/*
