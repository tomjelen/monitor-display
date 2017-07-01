deps:
	pip3 install unicornhathd requests requests-mock

test:
	python3 -m unittest discover --verbose --pattern '*_*tests.py'

run:
	python3 main.py

.PHONY: deps run test