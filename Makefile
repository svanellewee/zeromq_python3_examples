SYS_PYTHON=python3.6
VENV=venv
PIP=$(VENV)/bin/pip
PYTHON=$(VENV)/bin/python

$(VENV):
	$(SYS_PYTHON) -m venv $(VENV)
	$(PIP) install -U pip

depends: $(VENV)
	$(PIP) install zmq


clean-venv:
	rm -fr $(VENV)
