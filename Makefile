VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

all: install test run

$(VENV)/bin/activate: requirements.txt
	sudo apt-get update
	sudo apt-get install python3-venv
	python3 -m venv venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	
install: $(VENV)/bin/activate

test: $(VENV)/bin/activate
	$(PYTHON) test_app.py
	
run: $(VENV)/bin/activate
	$(PYTHON) app.py
