# py-api-automation
python, pytest, api, logging, configparser


How to run tests?
go to tests directory and simply run command "pytest"

If want to run on different environment
run command "pytest --testenv TEST1"

If want to run tests in parallel
1. install xdist by running command "pip install pytest-xdist"
2. run tests by command "pytest -n 3" 3 is number of parallel execution, you can see the difference if you have 100+ tests


