import sys
from DPOMDP_Writer.Reader import *
from DPOMDP_Writer.DPOMDPWriterMedium import DPOMDPWriterACC
import csv
#Call should look like python3 Getgit aResults.py filename start_state scenario_number
[cmd, filename, start_state, scenario_number] = sys.argv
result = "GMAA_" + filename + "_kGMAA_QMDP_h2_restarts1_k1_NoCache_BGIP-AM_AM_restarts10_JPol"
path_to_res = "~/.madp/results/" + filename + "/" + result

with open('dpomdp.csv', newline='') as csvfile:
    dreader = csv.reader(csvfile)
    data = list(dreader)
    print(data)
    machine_comm_actions = data[0]
    machine_mvmt_actions = data[1]
    human_comm_actions = data[2]
    human_mvmt_actions = data[3]
    modes = data[4]
    prob_dict = data[5]
    cost_dict = data[6]
    human_observations = data[7]
    machine_observations = data[8]

writer = DPOMDPWriterACC(machine_comm_actions, machine_mvmt_actions, human_comm_actions, human_mvmt_actions, modes,prob_dict,cost_dict,scenario_number, human_observations, machine_observations)

[h_tree, m_tree] = get_trees(result, len(human_observations), len(machine_observations))
graphs = writer.get_graph_viz_limit_branches(h_tree,m_tree, start_state)
print(graphs)