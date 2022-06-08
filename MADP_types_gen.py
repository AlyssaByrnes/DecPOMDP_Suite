import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in


solver_types = ["BFS", "AM", "CE", "MP", "BnB"]
GMAA_param = ["MAAstar", "FSPC", "kGMAA"]
q_heur = ["QMDP", "QPOMDP", "QBG", "QMDPc", "QPOMDPav", "QBGav", "QHybrid", "QPOMDPhybrid", "QBGhybrid", "QBGTreeIncPrune", "QBGTreeIncPruneBnB"]

count = 0

output = ""
for solver in solver_types:
    for gmaa_param in ["FSPC", "kGMAA"]:
        for q in q_heur:
            command = "timeout -k 1m 1m ../MADP/src/solvers/GMAA "
            command += "-G " + gmaa_param 
            command += " -B " + solver 
            command += " -Q " + q
            command += " MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2"
            output += command + "\n"
            count += 1

output = ""

for solver in solver_types:
    for gmaa_param in ["FSPC", "kGMAA"]:
        command = "timeout -k 1m 1m ../MADP/src/solvers/GMAA "
        command += "-G " + gmaa_param 
        command += " -B " + solver 
        command += " MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2"
        output += command + "\n"
        count += 1       

output = ""
for solver in solver_types:
    for q in q_heur:
        command = "timeout -k 5m 5m ../MADP/src/solvers/GMAA "
        command += "-G MAAstar"
        command += " -B " + solver 
        command += " -Q " + q
        command += " MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2"
        output += command + "\n"
        #remove optimal value database
        #output += "rm ~/.madp/results/GMAA/optimalValueDatabase\n"
        count += 1
        
f = open("ACCtest.sh", "w")
f.writelines(output)
f.close()

### Write evaluator for results

# Get list of all results
command = "ls -lrt >> lsOutput.log\n"
f = open("listresults.sh", "w")
f.writelines(command)
f.close()

# Write shell script that reads all file names and get results
output = "chmod +x listresults.sh \n"
output += "./listresults.sh"
y = "hkjjh_JPol"
print(y[-3:])

f = open("lsOutput.log")
