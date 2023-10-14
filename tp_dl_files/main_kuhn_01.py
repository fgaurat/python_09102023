"""
************************************************************************************
* Copyright (C) 2020 - KUHN SA - Electronics
*
* This document is KUHN SA property.
* It should not be reproduced in any medium or used in any way
* without prior written consent of KUHN SA
************************************************************************************
 """


# import time
import datetime
import os
import sys
import psutil


class Class_MemoryTracking: 
    
    def __init__(self, manager, testCaseObj):
        self.manager = manager
        self.param = self.manager.param.machineParam
        global TC
        TC = testCaseObj
        


    def record_memory_usage(self, Name_Script= "?ScriptName?"):
        
        try : # got some error sometimes, not finding any id -> Error and stop script... IDK WHY, not a big deal for the moment, use a "try" to avoid stopping script
            for id in psutil.pids(): # search all id 
                p = psutil.Process(id)
                if ( p.name() == 'python.exe' ): # search for the python.exe, we want the mem info only of this application
                    # get data 
                    mem_oct = p.memory_full_info().uss  # get memory usage of python in octet, transform in Mo
                    mem_prct = p.memory_percent() # get % mem usage of the process (% on the total ram available on the pc)

                    # process/formatting data
                    mem_Mo = mem_oct/(1024*1024) # transform octet to Mo
                    mem_32bits_prct = mem_oct*100/(2**31) # make a % with the 2^31 octet available on a 32bits target (=2Gb Ram)
                    # print ("Mem :", "%.2f"%mem_Mo,"Mo | %","glob ","%.1f"%mem_prct,"% |  % 32bits ", "%.1f"%mem_32bits_prct,"%",sep='')

        except:
            print(" >> Fail to Get Memory usage  <<")
            mem_Mo = -1  #return negative value if we can't get the real memory values
            mem_prct = -1
            mem_32bits_prct= -1 

        # Write the memory used in the .txt
        file = "C:/PROJECT/SOFTWARE/Python_MS600/Python_bench_data/Python_tests/Validation/Record_Memory_Used_By_Each_Scripts.txt"

        # get Date to give more info in the .txt
        date_now = datetime.datetime.now() 
        # print(type(date_now))
        # print(date_now.year, date_now.month, date_now.day, date_now.hour, date_now.minute, date_now.second) # to test/debug

        #prepare a string to write in the txt
        data_to_write_str = "["+"{:02d}".format(date_now.day)+"/"+"{:02d}".format(date_now.month)+"/"+str(date_now.year)+" at "+"{:02d}".format(date_now.hour)+":"+"{:02d}".format(date_now.minute)+":"+"{:02d}".format(date_now.second)+"] "+f"{Name_Script:<40}"+" |   Ram: "+"{:.2f}".format(mem_Mo)+" Mo   |   %Ram (total): "+"{:.1f}".format(mem_prct)+"%   |   %Ram (32bits): "+"{:.1f}".format(mem_32bits_prct)+"%"


        with open(file,'a') as handler: # Open a text file for appending text. If the file exists, the function append contents at the end of the file.
            handler.write(data_to_write_str) # write the data in the .txt
            handler.write('\n') # jump to the next line for the next time

        return mem_Mo, mem_prct, mem_32bits_prct

        



    def clean_Txt_MemoryTracking_File(self):
        file = "C:/PROJECT/SOFTWARE/Python_MS600/Python_bench_data/Python_tests/Validation/Record_Memory_Used_By_Each_Scripts.txt" # link to the .txt file
        with open(file,'w'): # opening a file with "w", delete all the text in the file
            pass