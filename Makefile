install:
    #install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
    #format code
	black *.py 
lint:
    #flake8 or #pylint
	# pylint --disable=R,C *.py 
test:
	# python -m pytest -vv  --cov=main 
deploy:
    #deploy
build:
	# build container
# all: install lint test  deploy