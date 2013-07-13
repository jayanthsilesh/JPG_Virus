import os
import re
import shutil



def go_into_dir(path_name):
	curdir=path_name
	all_files_dir=os.listdir(curdir)
	#print "\nAll the file present are ===",all_files_dir,"\n"

	for x in all_files_dir:
		complete_path_name=curdir+"\\"+x
		
		if(os.path.isdir(complete_path_name)):
			temp=str(complete_path_name).lower()
			m = re.search('(.*)jpg.files', temp)
			if m is None:
				go_into_dir(complete_path_name)
			else:
				print "Deleteing=>",complete_path_name

				#shutil.rmtree(complete_path_name)
			
		else:
			pass
			#print "FIle->",complete_path_name
			


if __name__=="__main__":
	curdir=os.getcwd()
	all_files=os.listdir(curdir)
	
	for x in all_files:
		complete_path=curdir+"\\"+x
		if(os.path.isdir(complete_path)):
			temp=str(complete_path).lower()
			m = re.search('(.*)jpg.files', temp)
			if m is None:
				go_into_dir(complete_path)
			else:
				print "Deleteing=>",complete_path
				#shutil.rmtree(complete_path)
		else:
			pass
			#print "FIle->",complete_path

