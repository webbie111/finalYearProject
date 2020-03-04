import obstacleMod.obstacleMod as oM
import imp
import sys
import subprocess
import changeConfig

sys.path.insert(1, 'C:/Users/Ed/Desktop/FinalYearProject/code/MengeUtils')
import AnalysisTask

# Run the simulator
subprocess.check_call([r"C:\Users\Ed\Desktop\FinalYearProject\code\Menge-master\Exe\menge.exe",
        "-p", r"C:\Users\Ed\Desktop\FinalYearProject\code\myAttempts\prototype.xml",
                "-o", r"C:\Users\Ed\Desktop\FinalYearProject\code\myAttempts\prototypeOutput.scb"])

# Change the location of the box obstacle
oM.changeBoxCoords(oM.getBoxCoords())

# Analyse the flow of the simulation
AnalysisTask.main()

# Change the analysis output location
# NOTE: could be using something like task.setTaskName( 'lores' ) in AnalysisTask
changeConfig.changeConfig(r'C:\Users\Ed\Desktop\FinalYearProject\code\myAttempts\prototype\flowConfig.cfg', 1)
