#!/usr/bin/python3
# Set up
import os	
import re
import sys
name=""
pexec=""

# Add to CheckInput
def addToCheckInput(location):
	for filename in os.listdir(location):
		appname=open(location+filename) 
		for line in appname:
			if "Name=" in line:
				name=line.rstrip().replace('Name=','')
				regex = re.compile('[^a-zA-Z]')
				nospacename=regex.sub('', name)
			if "Exec=" in line:
					pexec=line.rstrip().replace('Exec=','')
		# Create function
		with open("checkinput.py", "a") as myfile:
			myfile.write('	'+nospacename+'="'+name+'"\n')
			myfile.write("	if userinput in "+nospacename+":\n")
			myfile.write("		print('Program number: ', i)\n")
			myfile.write("		print('Program name: "+name+"')\n")
			myfile.write("		print('Exec command: "+pexec+"')\n")
			myfile.write("		i=i+1\n")
			myfile.write(r"		print('\n')")
			myfile.write("\n")
		print(name)

# This allows the second time of checkinput.py to be normal
def generatechecknumbergen(location):
	for filename in os.listdir(location):
		appname=open(location+filename) 
		for line in appname:
			if "Name=" in line:
				name=line.rstrip().replace('Name=','')
				regex = re.compile('[^a-zA-Z]')
				nospacename=regex.sub('', name)
			if "Exec=" in line:
					pexec=line.rstrip().replace('Exec=','')
		# Create function
		with open("checknumbergen.py", "a") as myfile:
			myfile.write('	'+nospacename+'="'+name+'"\n')
			myfile.write("	if userinput in "+nospacename+":\n")
			myfile.write("		print('"+pexec+"')\n")
			myfile.write(r"		print('\n')")
			myfile.write("\n")

home = os.path.expanduser("~")
addToCheckInput("/usr/share/applications/")
addToCheckInput(home+"/.local/share/applications/")

# Import function
from checkinput import checkinput

userinput=input("These are the programs you can launch. Pick one: ")

# Clears the screen, making the visibility of the new results much clearer
os.system('clear')

print("These are some of the programs that you can use:\n")

# Call Function
checkinput(userinput)

# Generates checknumbergen.py
with open("checknumbergen.py", "a") as myfile:
	myfile.write('def checknumbergen(userinput):\n')
generatechecknumbergen("/usr/share/applications/")
generatechecknumbergen(home+"/.local/share/applications/")
from checknumbergen import checknumbergen



# Change checkinput.py to be output of checkinput(userinput)
sys.stdout = open('checkinput.py', 'w')
checknumbergen(userinput)
sys.stdout.close()


# Removes blank lines
clean_lines = []
with open("checkinput.py", "r") as f:
    lines = f.readlines()
    clean_lines = [l.strip() for l in lines if l.strip()]
with open("checkinput.py", "w") as f:
    f.writelines('\n'.join(clean_lines))


#input("Go check your file corbin")

# Make changes to checkinput.py to be similar to 
'''
from checkinput import checknumber

userNumber=input("Pick a number to launch the program: ")

if userNumber==2:
		# Proper launching of bash command of pexec
'''



# Clear file to default
open('checknumbergen.py', 'w').close()
open('checkinput.py', 'w').close()
with open("checkinput.py", "a") as myfile:
	myfile.write("#!/usr/bin/python3\n")
	myfile.write("def checkinput(userinput):\n")
	myfile.write("	i=1\n")
