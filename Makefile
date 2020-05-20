freeze:
	pip-compile --no-index --output-file requirements.txt setup.py

freeze-upgrade:
	pip-compile --no-index --upgrade --output-file requirements.txt setup.py

.PHONY: freeze freeze-upgrade
