import re,os
from tkinter import *  
from tkinter.ttk import *

root = Tk()  
root.title('Update')
root.geometry('300x100+0+0') 
root.maxsize(300,170) 
str = StringVar()
Label(root,textvariable=str).pack(side=TOP,fill=X,padx=15,pady=5)
def pull():     
	# os.system("git pull")
	pull_result = os.popen('git pull').read()
	str.set("——————\nPull :\n" + pull_result + '——————')
def Commit():     
	add_result = os.popen('git add .').read()
	commit_result = os.popen('git commit -a -m "py"').read()
	str.set("——————\nAdd:\n" + add_result + 'Commit\n' + commit_result + '——————')
def push():	
	push_result = os.popen('git push -u origin master').read()
	str.set("——————\nPush:\n" + push_result + '——————')
func = Menu(root) 
func.add_command(label="Pull", command=pull) 
func.add_command(label="Commit", command=Commit) 
func.add_command(label="Push", command=push) 
func.add_command(label="Quit",command=root.quit)  
root.config(menu=func) 
mainloop()