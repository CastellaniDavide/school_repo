"""Test school_repo file
"""
from school_repo import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-11-30"

def test():
	"""Tests the school_repo function in the school_repo class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert school_repo.school_repo() == "school_repo", "test failed"
	#assert school_repo.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
