# write a make command that will install a python virtual environment from a requirements.txt
setup:
	python3 -m venv venv && \
	pip install --upgrade pip && \
	source venv/bin/activate && \
	pip install -r requirements.txt
run:
	source venv/bin/activate && \
	python3 main.py