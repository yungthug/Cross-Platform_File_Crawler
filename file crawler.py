import os,time

Tree=[]
Incomplete_Paths=[]

def Is_File(Path):
	return os.path.isfile(Path)

def File_Path_Handler(Dir):
	Branches=List_Items_In(Dir)
	for branch in Branches:
		Path=Dir+'/'+branch
		if Is_File(Path):
			Tree.append(Path.lower())
		else:
			Incomplete_Paths.append(Path)

def List_Items_In(Dir):
	Items=[]
	for x in os.listdir(Dir):
		Items.append(x)
	return Items

def Tree_Builder(Base_Dir):
	File_Path_Handler(Base_Dir)
	for x in Incomplete_Paths:
		File_Path_Handler(x)

Tree_Builder() #this is your main entry point
print Tree