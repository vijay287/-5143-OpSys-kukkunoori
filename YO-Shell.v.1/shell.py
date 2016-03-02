#Program name: shell.py
#Authors:Krishna bakka, Avinash Agumamidi, vijayaramakrishna kukkunoori
#This program implements shell commands cat,chmod,cd,cd .., cd ~, cp,ls including -l,-s,-a,-m,-c,
#  mv, rm,wc and wc -l commands.

#Note:::: inorder to run the shell give the command as a string that is place the string in double quotes


import os
import sys
import stat
import time
import shutil
from os.path import expanduser
from collections import Counter

#Name: historyManager
#Description: maintains history of shell commands
#methods:
#	push_command: adds commands to the history list
#	get_command: gets all the commands from the history
#	number_commands:gets number of commands in the history
class historyManager(object):
    def __init__(self):
        self.command_history = []

#Name:push_command
#Descriptions: adds commands to the history list
#params:takes the executed command
#returns: none
    def push_command(self,cmd):
        self.command_history.append(cmd)

#Name:get_commands
#Description: gets all the commands from the history
#params:none
#rerurns:list of command history
    def get_commands(self):
        return self.command_history

#Name:number_commands
#Description: gets number of commandsin the history
#params:none
#returns:number of commands        
    def number_commands(self):
        return len(self.command_history)

#Name:parserManager
#Description:contains functions related to the parsing the string
#contains:method like parse
class parserManager(object):
    def __init__(self):
        self.parts = []

#Name:parse
#Description:parses the given string into multiple strings
#takes one string and returns list of strings
    def parse(self,cmd):
        self.parts = cmd.split(" ")
        return self.parts
        
#Name:commandManager
#Description:executes the commands by using os interface, all the execution of the command is done here
#Methods: run_command,ls,longlist,lsBySize,lsByAtime,lsByMtime,lsByCtime,cat,chmod1,cddot,cdtilde,cddir,copy
#	move,remove,wordcount,linecount.
class commandManager(parserManager):
    def __init__(self):
        self.command = None

#Name:run_command
#Description: sends the given string to parse method and gets the list of parsed command
#returns the parsed list of the command
    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command

#Name:ls
#Description: lists all the files and directories in the woriking directory only,
#	because the method has the path of the working directory by default.
#returns none
#params: none
    def ls(self):
        for dirname, dirnames, filenames in os.walk('.'):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))
    
        # print path to all filenames.
        for filename in filenames:
            print(os.path.join(dirname, filename))
	
#Name:longlist
#Description: long lists all the files and directories in the directory giiven by the user. Will not take any path
#	but takes only the list in a list of all the files, usually derived using os.stat() and prints out by formatting them.
#	this charecteristics apply to other ls methods of the same class
#params: list of lists where the member list consists of list of various data like size, permissions, accessed time etc/
#Returns: none			
    def longlist(self,mylist):
		self.funcList = mylist
		for line in self.funcList:
			print("%25s %15s %15s %30s %30s %30s" % tuple(line))

#Name:lsBySize
#Description: long lists the files and directories sorted by size, same as longlist method it only takes list of lists.			
#params: list of list with the same charecteristics of list of lists given to longlist method
#returns:none
    def lsBySize(self,mylist):
		self.funcList = mylist
		sizesort = sorted(self.funcList,key = lambda x:x[1])	
		for line in sizesort:
			print("%25s %15s %15s %30s %30s %30s" % tuple(line))


#Name:lsByAtime
#Description: long lists the files and directories sorted by Access time of file
#params: list of lists
#returns:none			
    def lsByAtime(self,mylist):
		self.funcList = mylist
		atimeSort = sorted(self.funcList,key = lambda x:x[3])	
		for line in atimeSort:
			print("%25s %15s %15s %30s %30s %30s" % tuple(line))		


#Name:lsByMtime
#Description: long lists the files and directories sorted by Modified time
#params: takes the list of lists as lsByAtime method
#returns:none
    def lsByMtime(self,mylist):
		self.funcList = mylist
		mtimeSort = sorted(self.funcList,key = lambda x:x[4])	
		for line in mtimeSort:
			print("%25s %15s %15s %30s %30s %30s" % tuple(line))		

#Name:lsByCtime
#Description: long lists the files and directories sorted by changed time
#params: takes the list of lists as lsByMtime method
#returns: none
    def lsByCtime(self,mylist):
		self.funcList = mylist
		ctimeSort = sorted(self.funcList,key = lambda x:x[5])	
		for line in ctimeSort:
			print("%25s %15s %15s %30s %30s %30s" % tuple(line))	
		
		#print('\n'.join('{}:{}'.format(*k) for k in enumerate(sizesort)))	


#Name:cat
#Description: opens the given file to the console, if no file is present it creates the new one
#params:takes the filename as string
#return:none
    def cat(self,file):
        f = open(file,'r')
        print(f.read())
        
#Name:chmod1
#Description: changes the permissions of the given file, absolute path of the file is needed
#params:absolute path of the file
#returns:none
    def chmod1(self,mode,filename):
		os.chmod(filename,mode)
	
#Name:cddot
#Description: changes the directory up by one level
#params: none;
#returns:none
    def cddot(self):
		print("The current directory is")
		print(os.path.abspath(os.curdir))
		os.chdir("..")
		print("The changed directory is ")
		print(os.path.abspath(os.curdir))
	
#Name:cdtilde
#Description: changes the current directory to home directory
#params:none
#returns:none
    def cdtilde(self):
		print("The current directory is")
		print(os.path.abspath(os.curdir))
		self.dir = expanduser("~")
		os.chdir(self.dir)
		print("The changed directory is ")
		print(os.path.abspath(os.curdir))
	
#Name:cddir
#Description: changes the directory of the shell to the user provided directory 
#params:none
#returns:none
    def cddir(self,dirr):
		self.dir2=os.path.abspath(dirr)
		print("The current directory is")
		print(os.path.abspath(os.curdir))
		os.chdir(self.dir2)	
		print("The changed directory is ")
		print(os.path.abspath(os.curdir))

#Name:copy
#Description: copies the contents of one file to other
#params: names of source and destination file
#returns:none
    def copy(self,file1,file2):
		shutil.copy(file1,file2)

#Name: move
#Description: moves the contents of one file to other and deletes the original file
#params: file paths of source and destination files
    def move(self,file1,file2):
		shutil.move(file1,file2)
	
#Name: remove
#Description: deletes the file 
#params:path of the file needed to be deleted
#returns:none
    def remove(self,file1):
		os.remove(file1)
	
#Name:wordcount
#Description: counts the number of words in a given file
#params: path of the file
#returns num of lines
    def wordcount(self,file1):
		self.num = 0;
		self.file2 = open(file1)
		self.count = Counter(self.file2.read().split())
		for item in self.count.items():
			self.num = self.num + 1
			print("{}\t{}".format(*item))
		return self.num

#Name:lineCount
#Description: counts the number of lines in the given file
#params: path of the file
#returns:none
    def lineCount(self,file1):
		self.lines = sum(1 for line in open(file1)) 
		print("Number of lines is ", self.lines)

#Name:driver
#Description:drives the shell by calling the functions of commandManager and provides the
#	required data to the  functions	
class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0
 
#Name:runShell
#Description: runs the shell by taking the commands from the user, processing them and giving them 
# 	to the functions in the commandManger
#params:none
#returns:none
    def runShell(self):
        number_commands = 0
	while True:
		self.input = input("parser-$ ")         # get command
		self.history.push_command(self.input)   # put in history
		self.parts = self.commands.run_command(self.input)
			#print(parts)
		#self.filename=input("abc " )		
		#self.mode = input("qwer ")
		#self.commands.chmod1(self.filename,self.mode)
		
		if self.parts[0] == "cd":
			if self.parts[1] == "..":
				self.commands.cddot()
			elif self. parts[1] == '~':
				self.commands.cdtilde()
			else: 
				self.dir = self.parts[1]
				self.commands.cddir(self.dir)
				
		elif self.parts[0] == "cp":
			self.file1 = self.parts[1]				
			self.file2 = self.parts[2]
			self.commands.copy(self.file1,self.file2)

		elif self.parts[0] == "history":
			self.histList = self.history.get_commands()			
			for x in self.histList:
				print(x)
		elif self.parts[0] == "mv":
			self.file1 = self.parts[1]
			self.file2 = self.parts[2]
			self.file1 = os.path.abspath(self.file1)
			self.file2 = os.path.abspath(self.file2)
			self.commands.move(self.file1,self.file2)
		elif self.parts[0] == "rm":
			self.file1 = self.parts[1]
			self.file1 = os.path.abspath(self.file1)
			if os.path.isfile(self.file1):
				self.commands.remove(self.file1)
			else:
				print("File doesnt exist")
		elif self.parts[0] == "wc":
			
			if self.parts[1]=="-l":
				self.file1 =self.parts[2]
				self.file1= os.path.abspath(self.file1)
				self.commands.lineCount(self.file1)
			else:
				self.file1 = self.parts[1]
				self.file1 = os.path.abspath(self.file1)
				numfowords=self.commands.wordcount(self.file1)
			
		elif self.parts[0]=="ls":
			self.mypath = os.path.abspath('.')
			self.listinli = []
			print("%25s %15s %15s %30s %30s %30s" % ("File Name","Size","Permissions","Accessed","Modified","changed") )
			
			print("%25s %15s %15s %30s %30s %30s" % ("---------","--------------","-----------","------------------------","-------------------------","------------------------" ))
			
			for i in os.listdir(self.mypath):
				a = os.stat(os.path.join(self.mypath,i))
				self.listinli.append([i,a.st_size,oct(a.st_mode),time.ctime(a.st_atime),time.ctime(a.st_mtime),time.ctime(a.st_ctime)])
			if len(self.parts)==1:
				if self.parts[0] == "ls":
					self.commands.ls()
			else:
				self.flag = self.parts[1]
				if self.flag == "-l":
					self.commands.longlist(self.listinli)
				elif self.flag == "-s":
					self.commands.lsBySize(self.listinli)
				elif self.flag == "-a":
					self.commands.lsByAtime(self.listinli)
				elif self.flag == "-m":
					self.commands.lsByMtime(self.listinli)
				elif self.flag == "-c":
					self.commands.lsByCtime(self.listinli)
				else:
					print("Invalid flag")
		elif self.parts[0]=="cat":
			self.file1 = self.parts[1]
			self.commands.cat(self.file1)

		elif self.parts[0]=="chmod":
			self.permissions = ["777","755","700","666","644","600","777","755","700"]
			self.mode = self.parts[1]			
			if self.mode not in self.permissions:
				print("Not a valid permission")
			else:
				self.mode = int(self.parts[1])
				self.filename = self.parts[2]
				self.filename = os.path.abspath(self.filename)
				self.commands.chmod1(self.mode,self.filename)
							
		else:
			print("Command not found...")
		
	
if __name__=="__main__":
    d = driver()    
    d.runShell()

