import fileinput
from datetime import datetime, timedelta
import os

#dirname = os.path.dirname(__file__)
dirname = os.path.abspath(os.path.dirname(__file__))
filename = os.path.join(dirname, 'Data_Files\\ADR_BFR.txt')

text_to_search = 'APPOG'

print ('')
print ('**** Welcome to the Bulk File Replacer ! ****')
print ('')

replacement_text = p_id = input ('Enter the Property ID: ')

Compset_main = input ('Enter the Compset ID for Main Hotel: ')
Compset_Competitor_1 = input ('Enter the Compset ID for Competitor_1: ')
Compset_Competitor_2 = input ('Enter the Compset ID for Competitor_2: ')

Channel_ID_main = input ('Enter the Channel ID for Main Hotel: ')
Channel_ID_Competitor_1 = input ('Enter the Channel ID for Competitor_1: ')
Channel_ID_Competitor_2 = input ('Enter the Channel ID for Competitor_2: ')


with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    
    i = 150
    for line in file:
        
            d = datetime.today() - timedelta(days=i)          
            print(line.replace('LLLL', d.strftime("%d-%b-%y"),2).replace(text_to_search, replacement_text), end='')
            i=i-1
        
print('')
print('**** Please Wait! The relevant files are being replaced ****')
print('')
print ('Replace Completed for ADR_BFR')


#2 ELASTICITY**************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\ELASTICITY.txt')

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
        
            d = datetime.today() - timedelta(days=i)
            print(line.replace('LLLL', d.strftime("%d-%b-%y"),2).replace(text_to_search, replacement_text), end='')            
            i=i-1

print ('Replace Completed for ELASTICITY')



#3 LOC_RATE**************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\LOC_RATE.txt')

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
        
            d = datetime.today() - timedelta(days=i)          
            print(line.replace('LLLL', d.strftime("%d-%b-%y"),3).replace(text_to_search, replacement_text), end='')
            i=i-1
        

print ('Replace Completed for LOC_RATE')

#4 MKT_RESP_MODEL**************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\MKT_RESPONSE_MODEL.txt')

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
        
            d = datetime.today() - timedelta(days=i)
            print(line.replace('LLLL', d.strftime("%d-%b-%y"),1).replace(text_to_search, replacement_text).replace('UUUU', d.strftime("%d-%b-%y").upper(),1), end='')
            i=i-1
        

print ('Replace Completed for MKT_RESP_MODEL')


#5 OPTML_BFR **************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\OPTL_BFR.txt')

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
            d = datetime.today() - timedelta(days=i)
            print(line.replace('LLLL', d.strftime("%d-%b-%y"),3).replace(text_to_search, replacement_text), end='')
            i=i-1
        

print ('Replace Completed for OPTL_BFR')

#6 OPTL_BFR_CUR **************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\OPTL_BFR_CUR.txt')

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
            d = datetime.today() - timedelta(days=i)
            print(line.replace('LLLL', d.strftime("%d-%b-%y"),3).replace(text_to_search, replacement_text), end='')
            i=i-1
        

print ('Replace Completed for OPTL_BFR_CUR')

#7 PRICEOPT.MKT_RESP_MODEL **************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\PRICEOPT_MKT_RESP_MODEL.txt')

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
            d = datetime.today() - timedelta(days=i)
            print(line.replace('UUUU', d.strftime("%d-%b-%y").upper(),2).replace(text_to_search, replacement_text), end='')
            i=i-1
        

print ('Replace Completed for PRICEOPT.MKT_RESP_MODEL')

#8 PRICEOPT_MKT_RESP_MODEL_GRP **************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\PRICEOPT_MKT_RESP_MODEL_GRP.txt')


with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
            d = datetime.today() - timedelta(days=i)
            print(line.replace('UUUU', d.strftime("%d-%b-%y").upper(),2).replace(text_to_search, replacement_text), end='')
            i=i-1
        

print ('Replace Completed for PRICEOPT.MKT_RESP_MODEL_GRP')

#9 REMN_GRP_ADR_EST **************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\REMN_GRP_ADR_EST.txt')


with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
            d = datetime.today() - timedelta(days=i)
            print(line.replace('UUUU', d.strftime("%d-%b-%y").upper(),2).replace(text_to_search, replacement_text), end='')
            i=i-1
        

print ('Replace Completed for REMN_GRP_ADR_EST')

#10 RUBICON_EXPAND_Main_Hotel **************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\RUBICON_EXPAND_Main_Hotel.txt')


with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
            d = datetime.today() - timedelta(days=i)
            print(line.replace('UUUU', d.strftime("%d-%b-%y").upper(),4).replace(text_to_search, replacement_text).replace('92714', Compset_main), end='')
            i=i-1
        

print ('Replace Completed for RUBICON_EXPAND_Main_Hotel')

#11 RUBICON_EXPAND_Competitor_1 **************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\RUBICON_EXPAND_Competitor_1.txt')


with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
            d = datetime.today() - timedelta(days=i)
            print(line.replace('UUUU', d.strftime("%d-%b-%y").upper(),4).replace(text_to_search, replacement_text).replace('92714', Compset_Competitor_1), end='')
            i=i-1
        

print ('Replace Completed for RUBICON_EXPAND_Competitor_1')

#11 RUBICON_EXPAND_Competitor_2 **************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\RUBICON_EXPAND_Competitor_2.txt')


with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
            d = datetime.today() - timedelta(days=i)
            print(line.replace('UUUU', d.strftime("%d-%b-%y").upper(),4).replace(text_to_search, replacement_text).replace('92714', Compset_Competitor_2), end='')
            i=i-1
        

print ('Replace Completed for RUBICON_EXPAND_Competitor_2')

#12 RUBICON_LOCAL_Main_Hotel **************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\RUBICON_LOCAL_Main_Hotel.txt')

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
            d = datetime.today() - timedelta(days=i)
            print(line.replace('LLLL', d.strftime("%d-%b-%y"),3).replace(text_to_search, replacement_text).replace('1213622', Compset_main).replace('GDS', Channel_ID_main), end='')
            i=i-1
        

print ('Replace Completed for RUBICON_LOCAL_Main_Hotel')


#13 RUBICON_LOCAL_Competitor_1 **************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\RUBICON_LOCAL_Competitor_1.txt')


with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
            d = datetime.today() - timedelta(days=i)
            print(line.replace('LLLL', d.strftime("%d-%b-%y"),3).replace(text_to_search, replacement_text).replace('1213622', Compset_Competitor_1).replace('GDS', Channel_ID_Competitor_1), end='')
            i=i-1
        

print ('Replace Completed for RUBICON_LOCAL_Competitor_1')


#14 RUBICON_LOCAL_Competitor_2 **************************************************************************************

filename = os.path.join(dirname, 'Data_Files\\RUBICON_LOCAL_Competitor_2.txt')


with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    i = 399
    
    for line in file:
            d = datetime.today() - timedelta(days=i)
            print(line.replace('LLLL', d.strftime("%d-%b-%y"),3).replace(text_to_search, replacement_text).replace('1213622', Compset_Competitor_2).replace('GDS', Channel_ID_Competitor_2), end='')
            i=i-1
        

print ('Replace Completed for RUBICON_LOCAL_Competitor_2')
print ('')
print ('14 files replaced successfully')
print ('')

K = input ('Press Enter to exit. ')