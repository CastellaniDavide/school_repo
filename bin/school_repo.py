"""school_repo
"""
from github import Github
from collections import defaultdict
from os import path
from datetime import datetime
from time import sleep
from requests import get

__author__ = "help@castellanidavide.it"
__version__ = "01.04 2020-12-06"

TOKEN = "TODO"
ORGANIZATION = "TODO"
END_OF_ORGANIZATION_EMAIL = "TODO"
INITIAL_PART_OF_REPOS = ""

class school_repo:
	def __init__ (self, debug=False):
		"""Where it all begins
		"""
		# Start
		self.start = datetime.now()

		# Debug setup
		self.debug = debug

		# Open log file
		self.log = open(path.join(".", "log", "trace.log"), "a+")
		self.print(f"Start: {self.start}")
		self.read_input()

		# Made the login
		self.login()

		# Get online template for firts file
		self.get_tempate()

		# Create repos and brances
		self.create_repos()

		self.print(f"Ended: {datetime.now()}\nTotal time: {datetime.now() - self.start}\n")
		self.log.close()
	
	def login(self):
		"""Made the login
		"""
		self.g = Github(TOKEN).get_organization(ORGANIZATION)
		self.print("Login done")

	def read_input(self):
		"""Read the input file and transform it into a map
		"""
		self.input = defaultdict(list)
		for line in school_repo.csv2array(open(path.join(".", "flussi", "students.csv"), "r+").read())[1:-1]:
			self.input[line[1]].append(line[0])

		self.print("Input file readed")

	def csv2array(csv):
		"""Converts csv file to a py array
		"""
		array = []

		for line in csv.split("\n"):
			temp = []
			for item in line.replace(",", "','").split("','"):
				temp.append(item.replace('"', ""))
			array.append(temp)

		return array

	def create_repos(self):
		"""Create all repos and brances
		"""
		for repo_base_name in self.input:
			self.create_repo(repo_base_name)
			
	def create_repo(self, repo_base_name):
		""" Create a single repository with brances
		"""
		repo = ""
		for i in range(int(repo_base_name[0]) + 1):
			if repo == "":
				try:
					repo = self.g.get_repo(self.get_repo_name(repo_base_name, i))
					self.print(f"Get an old repo: {self.get_repo_name(repo_base_name, i)}")
				except:
					pass

		if repo == "":
			try:
				repo = self.g.create_repo(self.get_repo_name(repo_base_name))
				self.print(f"- Created repo for {repo_base_name} class, named {self.get_repo_name(repo_base_name)}")
			except:
				repo = self.g.get_repo(self.get_repo_name(repo_base_name))
				self.print(f"- Get access to the repo for {repo_base_name} class, named {self.get_repo_name(repo_base_name)}")

		try:
			repo.create_file("README.md", "Created initial file", self.template)
			self.print("\t- Created welcome file")
		except:
			self.print("\t- Welcome file already exists")
		
		main = self.get_main(repo)
		main.edit_protection(user_push_restrictions=[])

		for branch in self.input[repo_base_name]:
			try:
				repo.create_git_ref(ref=f'refs/heads/{branch}', sha=main.commit.sha)
				self.print(f"\t- Created branch user: {branch}")
			except:
				self.print(f"\t- Branch already exists: {branch}")

			try:
				self.g.invite_user(email=f"{branch}{END_OF_ORGANIZATION_EMAIL}", role="direct_member")
				self.print(f"\t- Invited new user: {branch}{END_OF_ORGANIZATION_EMAIL}")
			except:
				self.print(f"\t- The user is in org or the email is not correct: {branch}{END_OF_ORGANIZATION_EMAIL}")

	def get_repo_name(self, repo_base_name, last = 0):
		"""Get the complete the complete name of this year or of one of the last, using "last"
		"""
		return f"{INITIAL_PART_OF_REPOS}{self.start.year - last - (1 if self.start.month < 7 else 0)}-{self.start.year + (3 if int(repo_base_name[0]) in [1, 2] else 6) - int(repo_base_name[0]) + (1 if self.start.month < 7 else 0)}-{'B' if int(repo_base_name[0]) in [1, 2] else 'T'}-{repo_base_name[1:]}"

	def print(self, message):
		"""Print wanted message
		"""
		self.log.write(f"{message}\n")
		if self.debug : print(message)

	def get_main(self, repo):
		"""Returns main
		"""
		try:
			return repo.get_branch("main")
		except:
			sleep(1)	# Wait a while
			self.print("\tI'm waiting and searching main branch")
			return self.get_main()

	def get_tempate(self):
		"""Gets template
		"""
		self.template = get("https://raw.githubusercontent.com/CastellaniDavide/school_repo/main/docs/template.md").text
		
if __name__ == "__main__":
	# Checker
	assert(TOKEN != "TODO")
	assert(ORGANIZATION != "TODO")
	assert(END_OF_ORGANIZATION_EMAIL != "TODO")

	# Run code
	school_repo(True)
