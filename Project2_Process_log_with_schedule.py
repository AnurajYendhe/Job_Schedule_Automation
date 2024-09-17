# Description :- Process Automation with job schedule - Accept directory name and time interval from user and create a log file which conatin info about running process after specified time interval.

######################################################################
# importing requried package
######################################################################
import os
import time
import psutil
import schedule
from sys import *
from datetime import datetime

######################################################################
# Function name :- printResult
# Description :- generate record of running process
# Input :- Path of directory,list of process info
# Output :- generate log file to mantain the record of running process
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def printResult(DirName,listprocess):
    separator = "-" * 100
    log_path = os.path.join(DirName,"Marvellous"+str(datetime.now().strftime("%Y-%m-%d -%H-%M-%S"))+".log")
    f = open(log_path,'w')
    f.write(separator + "\n")
    f.write("Processur log : "+time.ctime()+"\n")
    f.write(separator + "\n")
    f.write("\n")

    for element in listprocess:
        f.write("%s\n"%element)

    f.write("\n") 
    f.write(separator + "\n")
    f.write("Total numbers of running process is : %s"%len(listprocess)+ "\n")
    f.write(separator + "\n")
    f.close()

    print("Log file successfully generated at location %s" %(log_path)) 
    print("That contain info about running.")

######################################################################
# Function name :- checkAbs
# Description :- to check directory path is absolute path or not
# Input :- Path of file
# Output :- return True(path is absolute) / False(path is not absolute)
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def checkAbs(DirName):
    result = os.path.isabs(DirName)
    return result

######################################################################
# Function name :- createAbs
# Description :- to create absolute path of directory
# Input :- Path of file
# Output :- Absolute path of directory
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def createAbs(DirName):
    result = os.path.abspath(DirName)
    return result

######################################################################
# Function name :- checkDir
# Description :- to check directory exists or not
# Input :- Path of file
# Output :- return True( path is exists) / False(path is not exists)
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def checkDir(DirName):
    result = os.path.exists(DirName)
    return result

######################################################################
# Function name :- createDir
# Description :- to create directory
# Input :- Name of directory
# Output :- create directory of specified name
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def createDir(DirName):
    try:
        os.mkdir("Marvellous") 
    except:
        pass
        
######################################################################
# Function name :- ProcessDisplay
# Description :- To fetch the info about running process
# Input : - path of directory
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def ProcessDisplay():
    DirName = argv[1]
    flag = checkAbs(DirName)
    if(flag == False):
        DirName = createAbs(DirName)
    
    exist = checkDir(DirName)
    if not exist:
            createDir(DirName)

    if(exist == True):
        listprocess = list()
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid','name','username'])
                listprocess.append(pinfo)
            except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        printResult(DirName,listprocess)

    else:
        print("Error : Invalid inputs")
        exit()

######################################################################
# Function name :- main
# Description :- Main function from where execution starts
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def main():
    print("-------------Automation using Python------------")
    print("--------Process Automation with Job Schedule--------")
    print("Name of script : ",argv[0])
    print("    ")

    if(len(argv) == 2): # validation
        if((argv[1] == "-H") or (argv[1] == "-h")): # flag for help
            print("Help : This automation script is use create a log file after specified time interval which contain info about running process")
            exit()

        elif((argv[1] == "-U") or (argv[1] == "-u")): # flag for usage
            print('Usage : Name_of_script.py Path_of_directory Time_interval')
            print('Example : Project2_Process_log_with_schedule.py "Anuraj" 50')
            exit()

        else:
            print("Error : invalid arguments.")

    elif(len(argv) == 3):
        try:
            schedule.every(int(argv[2])).minutes.do(ProcessDisplay)
            while True:
                schedule.run_pending()
                time.sleep(1)

        except ValueError:
            print("invalid inputs")

        except Exception as Err:
            print("invalid inputs ",Err)

    else:
        print("Error : invalid numbers of arguments")
        exit()

######################################################################
# Application stater
######################################################################
if __name__ == "__main__":
    main()
