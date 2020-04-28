# py-api-automation
python, pytest, api, logging, configparser


How to run tests?
go to tests directory and simply run command "pytest"

If want to run on different environment
run command "pytest --testenv TEST1"

If want to run tests in parallel
1. install xdist by running command "pip install pytest-xdist"
2. run tests by command "pytest -n 3" 3 is number of parallel execution, you can see the difference if you have 100+ tests

cache provides two command line options to rerun failures from the last pytest invocation:

1. --lf, --last-failed - to only re-run the failures.
2. --ff, --failed-first - to run the failures first and then the rest of the tests.
3. For cleanup (usually not needed), a --cache-clear option allows to remove all cross-session cache contents ahead of a test run.

If you want to generate pytest html report
1. install pytest-html plugin by running command "pip install pytest-html"
2. run tests by command "pytest --html=../log/pytest_report.html"

If you want to run grouped tests
run command "pytest -m smoke --html=../log/pytest_report.html"    // smoke is the group name marked by "@pytest.mark.smoke"
