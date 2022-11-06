install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		sudo apt-get install sqlite3

test:
	python -m pytest -vv test_*.py

format:	
	black *.py dblib/*py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

all: install lint test format