import gc
import os


class Test :

    def __init__(self, TC):

        # TC.addReqs(["Reqs1", "Reqs2","Reqs3"])
        TC.scriptVersion("1.0")

        ###############
        ### IMPORTS ###
        ###############

        self.param = TC.manager.param.machineParam
        self.opVar = TC.manager.param.opVar
        name_file = os.path.splitext(os.path.basename(__file__))[0] #used to get the file name without extension ".py"

        #################
        ### VARIABLES ###
        #################


        ######################
        ### INITIALISATION ###
        ######################

        TC.startInit()
        TC.stopInit()

        ############
        ### TEST ###
        ############

        TC.startMainGroup("Test Graph")
        
        # TC.specFunc("MemoryTracking/clean_Txt_MemoryTracking_File", "clean_Txt_MemoryTracking_File") # Clean the .txt
        TC.specFunc("MemoryTracking/record_memory_usage", "record_memory_usage", name_file)

        
        for i in range(25):
            
            xVals = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            yVals = [5,5,5,5,5,5,5,5,5,5,5.6,6.4,7,7.5,7.8,8,8.2,8.4,8.5,8.5,8.5]
            # #Create a graph
            TC.graph.start()
            # # Add curves
            TC.graph.addCurve("Vitesse", xVals, yVals,[3,"b","-"],True)
            TC.graph.addCurve("Changement consigne",[9,9], [0,100],[1.5,"g","-"],False)
            TC.graph.addCurve("Consigne",[0,9,9,20], [5,5,8.5,8.5],[1.5,"r","--"],False)
            #Activate grid and parameter the tool
            TC.graph.grid(True)
            TC.graph.params("Test d'acceleration","Time", "Speed", True)
            TC.graph.axesParam([0,20],[4,10])
            TC.graph.addTxt(1,5.3,"Consigne de départ : 5")
            TC.graph.addTxt(9.1,8.2,"Nouvelle consigne : 8.5")
            TC.graph.save("AccelerationTest")

            TC.specFunc("MemoryTracking/record_memory_usage", "record_memory_usage", name_file)

        TC.stopMainGroup("Test Graph")

        Memory_Data_aint8 = TC.specFunc("MemoryTracking/record_memory_usage", "record_memory_usage", name_file)
        TC.description = str(int(Memory_Data_aint8[0]))+"Mo ("+"{:.1f}".format(Memory_Data_aint8[2])+" %)"
        
        # del (TC.graph)
        # gc.collect()
        # m.Stop_Monitoring_Memory()
        #Add other main groups....

        ##############
        ### ENDING ###
        ##############

        TC.startEnding()
        



        TC.stopEnding()
