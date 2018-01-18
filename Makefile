test:
	coverage run --source=./ -m unittest discover --start-directory ./tests -p "*.py"


test_report: test
	coverage report -m
