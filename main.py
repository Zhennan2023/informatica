# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:17:32 2019

@author: paprasad
"""

from pmcmd import *
from log_analyser import *
from prediction_service import * 





'''


fetch_log(Domain_name="Domain_item-s65484",username = "pawan",pswd = "pawan",frmt = "TEXT",location = "./Logs/", IS = "INT_SRVC",
              IR = "INFA_REP",FOLDER = "INFA_FOLDER",session = "s_m_CrDbStatsment" ,wf = "wf_m_CrDbStatsment"):
'''
log_file = fetch_log(wf = "wf_m_CrDbStatsment",session= "s_m_CrDbStatsment") 
print (log_file)
error_matrix  = readLogError(log_file)
error_matrix[8] = error_matrix[8]+' '+error_matrix[9]+' '+error_matrix[10]

error_matrix = error_matrix.drop([9,10] ,axis = 1)


error_type = error_predition(error_matrix)
#print(error_matrix[[7,8]])

error_function_mapping['FR_3065']()