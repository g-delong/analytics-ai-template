setup:
	pip install --upgrade pip wheel setuptools
	pip install -r requirements_dev.txt
	pip install -r requirements.txt
	zenml integration install s3 aws -y

format:
	isort src
	isort run.py
	black src
	black run.py
