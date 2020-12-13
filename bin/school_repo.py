"""school_repo
by Castellani Davide
"""
from github import Github
from collections import defaultdict
from os import path
from datetime import datetime
from time import sleep
from requests import get
from threading import Thread, active_count

__author__ = "help@castellanidavide.it"
__version__ = "03.01 2020-12-13"

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
		self.log = open(path.join(".", "log", f"trace_{int(self.start.timestamp())}.log"), "a+")
		self.log.write("Execution_code,Repo,Message,time")
			
		self.print(f"Start: {self.start}")
		self.read_input()

		# Made the login
		self.login()

		# Get online template for firts file
		self.get_tempate()

		# Create repos and brances
		Thread(target = self.create_repos).start()

		# Add teachers to the organization
		Thread(target = self.add_teachers).start()

		while (active_count() != 1) : print(active_count()) # Wait the end
		self.print(f"Ended: {datetime.now()}")
		self.print(f"Total time: {datetime.now() - self.start}\n")
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
		for line in self.csv2array(open(path.join(".", "flussi", "students.csv"), "r+").read())[1:-1]:
			self.input[line[1]].append(line[0])

		self.teachers = []
		for line in open(path.join(".", "flussi", "teachers.csv"), "r+").read().split("\n")[1:-1]:
			self.teachers.append(line)

		self.print("Input file readed")

	def csv2array(self, csv):
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
			Thread(target = self.create_repo, args=(repo_base_name,)).start()
			
	def create_repo(self, repo_base_name):
		""" Create a single repository with brances
		"""
		repo = ""
		for i in range(int(repo_base_name[0]) + 1):
			if repo == "":
				try:
					repo = self.g.get_repo(self.get_repo_name(repo_base_name, i))
					self.print(f"Get an old repo: {self.get_repo_name(repo_base_name, i)}", repo=repo)
				except:
					pass

		if repo == "":
			try:
				repo = self.g.create_repo(self.get_repo_name(repo_base_name))
				self.print(f"Created repo for {repo_base_name} class, named {self.get_repo_name(repo_base_name)}", repo=repo)
			except:
				repo = self.g.get_repo(self.get_repo_name(repo_base_name))
				self.print(f"- Get access to the repo for {repo_base_name} class, named {self.get_repo_name(repo_base_name)}", repo=repo)

		try:
			repo.create_file("README.md", "Created initial file", self.template)
			self.print("\t- Created welcome file", repo=repo)
		except:
			self.print("\t- Welcome file already exists", repo=repo)

		main = self.get_main(repo)
		main.edit_protection(user_push_restrictions=[])

		for branch in self.input[repo_base_name]:
			Thread(target=self.branch, args=(repo, main, branch))

	def branch(self, repo, main, branch):
		""" Understand if branch exist and if not create it and add user
		"""
		try:
			repo.git.checkout(branch)
			self.print(f"\t- Branch and User already exists: {branch}", repo=repo)
		except repo.exc.GitCommandError:
			Thread(target = self.my_create_branch, args=(repo, branch, main)).start()
			Thread(target = self.add_student, args=(repo, branch, main)).start()

	def my_create_branch(self, repo, branch, main):
		"""Try to create the branch
		"""		
		try:
			repo.create_git_ref(ref=f'refs/heads/{branch}', sha=main.commit.sha)
			self.print(f"\t- Created branch user: {branch}", repo=repo)
		except:
			sleep(1) # Wait a moment
			self.my_create_branch(repo, branch, main)

	def add_student(self, repo, branch, main):
		"""Try to add a new student to the repo
		"""
		try:
			self.g.invite_user(email=f"{branch}{END_OF_ORGANIZATION_EMAIL}", role="direct_member")
			self.print(f"\t- Invited new user: {branch}{END_OF_ORGANIZATION_EMAIL}", repo=repo)
		except:
			sleep(1) # Wait a moment
			self.add_student(repo, branch, main)

	def add_teachers(self):
		"""Add teachers to the repo
		"""
		for teacher in self.teachers:
			try:
				self.g.invite_user(email=f"{teacher}", role="direct_member")
				self.print(f"\t- Invited new user: {teacher}")
			except:
				self.print(f"\t- The user is in org or the email is not correct: {teacher}")

	def get_repo_name(self, repo_base_name, last = 0):
		"""Get the complete the complete name of this year or of one of the last, using "last"
		"""
		return f"{INITIAL_PART_OF_REPOS}{self.start.year - last - (1 if self.start.month < 7 else 0)}-{self.start.year + (3 if int(repo_base_name[0]) in [1, 2] else 6) - int(repo_base_name[0]) + (1 if self.start.month < 7 else 0)}-{'B' if int(repo_base_name[0]) in [1, 2] else 'T'}-{repo_base_name[1:]}"

	def print(self, message, repo="No repo"):
		"""Print wanted message
		"""
		if self.debug : print(f""""{self.start.timestamp()}","{str(repo).replace('Repository(full_name="', '').replace('")', '')}","{message}","{datetime.now().timestamp()}" """)
		self.log.write(f""""{self.start.timestamp()}","{str(repo).replace('Repository(full_name="', '').replace('")', '')}","{message}","{datetime.now().timestamp()}"\n""")

	def get_main(self, repo):
		"""Returns main
		"""
		try:
			return repo.get_branch("main")
		except:
			sleep(1)	# Wait a while
			self.print("I'm waiting and searching main branch", repo=repo)
			return self.get_main(repo)

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
