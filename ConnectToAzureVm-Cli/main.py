import os
import pymssql
import pandas as pd
import subprocess, sys

def GetAllData():
    server = "mssql.bryan86.hu"
    user = "demo"
    password = "Demo1234#"

    conn = pymssql.connect(server, user, password, "VM")
    cursor = conn.cursor()
    cursor.callproc("GetAllData")
    row = cursor.fetchall()
    conn.close()
    return row

ad_domain =""

#Check for existing XML file
def check_xml():
    xml_file = ""
    for file in os.listdir("./"):
        if file.endswith(".xml"):
            print("Used XML file: " + file)
            xml_file = file
    return xml_file

def ShowMenu():
    data = GetAllData()
    df = pd.DataFrame(data, columns=['ID', 'Hostname','Location', 'Resource', 'Domain', 'ADDomain', 'PEM'])
    print(df)

os.system("cls")
print ("Please select Mode (RDP -> r, SSH -> s, PSSession -> p)")

mode = input('Mode:')

# Mode s = SSH
if (mode == "s"):
    sql_data = GetAllData()
    ShowMenu()

    #Get required data
    id = input('Please enter ID:')
    id = int(id)
    hostname = sql_data[id][4]
    pem = sql_data[id][6]
    username = input('Please enter Username:')
  
    #run ssh command
    os.system("ssh -i " + pem + " " + username + "@" +hostname)

#Mode r = RDP
elif (mode == "r"): 
    ShowMenu()

    #Get data for RDP connection
    sql_data = GetAllData()
    id = input('Please enter ID:')
    id = int(id)
    hostname = sql_data[id][4]
    ad_domain = sql_data[id][5]

    #XML credential file not exists
    xml= check_xml()
    
    if xml =="":

        # Do you want create a new?
        print("[Warning] Your credential file not exist!")
        choice= input ("Do you want to Create a new XML file? (y/n)")

        if (choice =="Y" or choice == "y"):
            if (ad_domain !="-"):
                 p = subprocess.Popen(["powershell.exe", "./rdp.ps1","-hostname",hostname,"-addomain",ad_domain], stdout=sys.stdout) 
                 p.communicate()
            else:
                p = subprocess.Popen(["powershell.exe", "./rdp.ps1","-hostname",hostname], stdout=sys.stdout) 
                p.communicate()
    else:
        if (ad_domain !="-"):
            p = subprocess.Popen(["powershell.exe", "./rdp.ps1","-hostname",hostname,"-xml",xml,"-addomain",ad_domain], stdout=sys.stdout) 
            p.communicate()
        else:
            p = subprocess.Popen(["powershell.exe", "./rdp.ps1","-hostname",hostname,"-xml",xml], stdout=sys.stdout) 
            p.communicate()

elif (mode == "p"):

    ShowMenu()

    #Get data for RDP connection
    sql_data = GetAllData()
    id = input('Please enter ID:')
    id = int(id)
    hostname = sql_data[id][4]

    xml= check_xml()
    # Do you want create a new?

    if xml =="":

        print("[Warning] Your credential file not exist!")
        choice= input ("Do you want to Create a new XML file? (y/n)")

        if (choice =="Y" or choice == "y"):            
                p = subprocess.Popen(["powershell.exe", "./pssession.ps1","-hostname",hostname], stdout=sys.stdout) 
                p.communicate()            
    else:
        p = subprocess.Popen(["powershell.exe", "./pssession.ps1","-hostname",hostname,"-xml",xml], stdout=sys.stdout) 
        p.communicate()
