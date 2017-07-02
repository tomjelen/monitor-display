deps:
	pip3 install unicornhathd requests

test_deps: deps
	pip3 install requests-mock sniffer

test_watch: test_deps
	sniffer

test: test_deps
	python3 -m unittest discover --verbose --pattern '*_*tests.py'

run:
	python3 app.py

.PHONY: deps test_deps test test_watch run
