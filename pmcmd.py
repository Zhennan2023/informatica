# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:38:52 2019

@author: paprasad
"""

import os 
import datetime

os.system('mkdir test')

time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
timestamp = str(time)
'''


C:\Informatica\9.6.1\server\bin>infacmd.bat 
getSessionLog -dn "Domain_item-s65484" -un pawan -pd pawan -fm Text -lo "d:\Profiles\paprasad\INFA\Pawan\src\logs.txt" -is INT_SRVC -rs INFA_REP -ru pawan -rp pawan -fn 
 "INFA_FOLDER" -ss "s_m_CrDbStatsment" -wf "wf_m_CrDbStatsment"
'''




def excute_commands(cmd):
    os.system(cmd)

def fetch_log(Domain_name="Domain_item-s65484",username = "pawan",pswd = "pawan",frmt = "TEXT",location = "./Logs/", IS = "INT_SRVC",
              IR = "INFA_REP",FOLDER = "INFA_FOLDER",session = "s_m_CrDbStatsment" ,wf = "wf_m_CrDbStatsment"):
    
    
    session_file_name  = session+timestamp+'.txt'
    location = location+session_file_name
    
    command_srt = "C:\Informatica\9.6.1\server\\bin\infacmd.bat getSessionLog -dn "+Domain_name+" -un "+username+" -pd "+pswd+" -fm "+frmt+" -lo "+location+" -is "+IS+" -rs "+IR+" -ru "+username+" -rp "+pswd+" -fn "+FOLDER+" -ss "+session+" -wf "+wf
    excute_commands(command_srt)
    
    #print(command_srt)
   
   
    return location



    