from os import path
from datetime import datetime
from school_repo import school_repo
from sys import argv

def test_school_repo_():
    """My tester
    """
    # Change part of file
    assert(argv[1] != "${{ secrets.TOCKEN }}")
    modified = open(path.join('.', 'bin', 'school_repo.py'), 'r+').read().replace('TOKEN = "TODO"', f'TOCKEN = "{argv[1].replace('"', '').replace("'", "")}"').replace('ORGANIZATION = "TODO"', f'ORGANIZATION = "CastellaniDavideTest"').replace('END_OF_ORGANIZATION_EMAIL = "TODO"', f'END_OF_ORGANIZATION_EMAIL = ""').replace('INITIAL_PART_OF_REPOS = "TODO"', f'INITIAL_PART_OF_REPOS = "{int(datetime.now().timestamp())}"')
    open(path.join('.', 'bin', 'school_repo.py'), 'w+').write(modified)
    
    # Try code
    school_repo()

if __name__ == "__main__":
    test_school_repo_()
