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
3. Do test function using pytest
   ```shell
   # unittest will ignore pytest testcases 
   python -m unittest -v .\tests\test_learn_unittest\test_check_even_or_odd.py

   # pytest tests both unttest.TestCase and pytest both testcases
   # or
   pytest -v tests\test_learn_unittest\test_check_even_or_odd.py
   # or 
   pytest -W ignore -v tests\test_learn_unittest\test_check_even_or_odd.py
   # or
   pytest -q tests\test_learn_unittest\test_check_even_or_odd.py
   ```
   
### Advanced Topic:
Ids | topic | Details | Remarks
--- | ----- | ------- | -------
1 | @pytest.mark.parametrize | parameterized multiple testcases with expected result. | 
2 | unittest.TestCase().assertRaises() and pytest.raises | test exception raised from the function |
3 | mock and patch | |