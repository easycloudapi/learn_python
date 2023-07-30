## Unit test

### Ref:
1. python unittest doc
   

### Pre-requisite
1. Install Python Packages
	```shell
	pip install pytest 
	```
2. *(optional)* Check the sys.path should point to root dir of the application `(local_python_project)` else
   it will show `no module found - error`
3. Do test function using pytest or unittest
	```shell
	# unittest will ignore pytest testcases 
	python -m unittest -v .\tests\test_learn_unittest\test_check_even_or_odd.py

	# pytest tests both unttest.TestCase and pytest both testcases
	# or
	pytest -v tests\test_learn_unittest\test_check_even_or_odd.py
	# or 
	pytest -W ignore -v tests\test_learn_unittest\test_check_even_or_odd.py
	```

### pytest options
    ```shell
    # pytest tests specific func using "::"
    pytest -v .\tests\test_learn_unittest\test_check_even_or_odd.py::test_check_even_or_odd
    ```

    ```shell
    # pytest tests with only "negative" or "wrong" keyword
    # -v: verbose, -k: keyword
    pytest -v -k "negative or wrong"
    ```

	```shell
	# pytest mark, use @pytest.mark.parametrize or @pytest.mark.positive
	# -m: mark
	pytest -W ignore -v -m parametrize
	# or
	pytest -W ignore -v -m positive

	# -x: any failed test occured, pytest will stop further
	# --tb=no : will stop display the assert error/stack trace
	pytest -v -x --tb=no

	# --maxfail: count, will execute the testcase till the time its reaches to maxfail count
	pytest --maxfail=2

	# -s or --capture=no, will show to print statement written inside testcases
	pytest -v -s 
	# or 
	pytest -v --capture=no

	# -q: only show how much testcases passed at what time, no further info will display
	pytest -q
	```
   
### Advanced Topic:
Ids | topic | Details | Remarks
--- | ----- | ------- | -------
1 | @pytest.mark.parametrize | parameterized multiple testcases with expected result. | [@pytest.mark.parametrize](tests/test_learn_unittest/test_check_even_or_odd.py)
2 | @pytest.mark.<mark_name> | run those testcases which has marked by <mark_name> | [@pytest.mark.<mark_name>](tests/test_learn_unittest/test_check_even_or_odd.py)
3 | @pytest.mark.skip(reason="skip reason") or unittest.skip() | to skip the pytest testcases | 
4 | @pytest.mark.skipif(<bool expression>, reason="skip reason") | to skip the pytest testcases based on bool expression | [@pytest.mark.skipif(<bool expression>, reason="skip reason")](tests/test_learn_unittest/test_check_even_or_odd.py)
5 | pytest.fixture | |
6 | setup() and teardown() methods | This is the fixtures of unittest. fixture is function/method that runs before and after a block of test code executes. It can be module or class or method level | [setup() and teardown()](learn_unittest/check_jsondata_file.py)
7 | unittest mock and patch | its require when the functionaly depends on other outside functionality | [mock_&_patch](tests/test_learn_unittest/test_check_api_for_mocking.py)
8 | unittest.TestCase().assertRaises() and pytest.raises | test exception raised from the function |
<ids> | <topic> | <details> | <remarks>
