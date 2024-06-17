VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

all: install test

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	
install: $(VENV)/bin/activate

test: $(VENV)/bin/activate
	$(PYTHON) test_app.py
	
run: $(VENV)/bin/activate
	$(PYTHON) app.py
