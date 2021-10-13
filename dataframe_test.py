import sys
from dataframe import main

def test_main_empty() -> None:
    assert main('/home/sergio/dev/python/projects/test_pandas/italy.csv') == ''