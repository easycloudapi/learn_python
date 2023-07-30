# Learn Python

## Pre-requisite:
1. Create and Activate the Virtual Environment 
    ```shell
    python -m virtualenv env
    .\env\Scripts\activate
    ```
2. *(optional)* if any error while activate the virtual env, follow below steps-
    ```shell 
    get-ExecutionPolicy
    Set-ExecutionPolicy Unrestricted -Scope Process  # if its restricted, then execute this command
    ```
3. Install the python dependencies
    ```shell
    python -m pip install --upgrade pip 
    pip install -r .\requirments.txt
    ```

## Unit Test
1. [Learn Unit Test](Readme_docs/Learn_Unittest_README.md)
2. [Unittest Code Sample](tests/test_learn_unittest)

## Github
1. [Learn GitHub](Readme_docs/github_README.md)