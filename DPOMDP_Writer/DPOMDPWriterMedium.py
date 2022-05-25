
import itertools
import copy
#from help_methods import *
from DPOMDP_Writer.ExtractCSV import latex_to_table
import sys
sys.path.append("..")
from ArrayTree import ArrayTree



mode_change_table = latex_to_table("DPOMDP_Writer/TransitionLatexClean.csv")

class DPOMDPWriterACC:

    def __init__(self,mach_comm_acts, mach_move_acts,hum_comm_acts,hum_move_acts,modes,prob_dict,cost_dict, scenario_number, human_observations, machine_observations):
        #since this is medium, there is only 1 scenario
        self.states = modes
        self.human_actions = list(itertools.product(hum_move_acts, hum_comm_acts))
        self.machine_comm_actions = mach_comm_acts
        self.machine_actions = list(itertools.product(mach_move_acts, mach_comm_acts))
        #self.decpomdp = DecPOMDP_medium(mach_comm_acts, mach_move_acts,hum_comm_acts,hum_move_acts,prob_dict,modes,scenario_number, cost_dict)
        self.costs = cost_dict
        self.scenario = scenario_number
        self.prob_dict = prob_dict
        self.scenario_number = scenario_number
        self.human_observations = human_observations
        self.machine_observations = machine_observations


    def get_allowed_machine_actions(self,mode):
        sc = (mode == "speedcontrol")
        follow = (mode == "following")
        if sc | follow :
            allowed_mvmts = ["accel", "decel", "maintainspeed"]
        else:
            allowed_mvmts = ["none"]
        return list(itertools.product(allowed_mvmts,self.machine_comm_actions))
    
    def get_unallowed_machine_actions(self,mode):
        sc = (mode == "speedcontrol")
        follow = (mode == "following")
        if sc | follow :
            unallowed_mvmts = ["none"]
        else:
            unallowed_mvmts = ["accel", "decel", "maintainspeed"]
        return list(itertools.product(unallowed_mvmts,self.machine_comm_actions))

    def all_states_to_str(self):
        state_str = "states:"
        for state in self.states:
            state_str += " " + state
        #print(state_str)
        return state_str

    def state_to_str(self, state):
        return state

    def action_to_str(self,action):
        [mvmt, comm] = action
        return mvmt + "-" + comm

    def action_list_to_str(self, action_list):
        action_str = ""
        for act in action_list:
            action_str += self.action_to_str(act) + " "
        return action_str[:-1]

    def list_to_str(self, inp_list):
        output_str = ""
        for elem in inp_list:
            output_str += elem + " "
        return output_str[:-1]

    def get_safety(self,human_action, machine_action):
        #input PHYSICAL MOVEMENT actions as human_action and machine_action
        scenario = self.scenario
        anti_decel = ["accel", "maintainspeed"]
        anti_accel = ["decel"]
        if (scenario == 1) | (scenario == 2) | (scenario == 5):
            if (human_action == "decel") & ~(machine_action in anti_decel):
                return True
            elif (machine_action == "decel") & ~(human_action in anti_decel):
                return True
            else:
                return False
        elif (scenario == 3) | (scenario == 7):
            if (human_action == "decel") & ~(machine_action in anti_decel):
                return False
            elif (machine_action == "decel") & ~(human_action in anti_decel):
                return False
            else:
                return True
        elif (scenario == 4) | (scenario == 8):
            if (human_action == "accel") & ~(machine_action in anti_accel):
                return True
            elif (machine_action == "accel") & ~(human_action in anti_accel):
                return True
            else:
                return False
        elif (scenario == 6):
            return False
        else:
            print("ERROR! Unrecognized scenario!")

    def get_cost(self, human_action, machine_action, start_state):
        [hum_mvmt, hum_comm] = human_action
        [mach_mvmt, mach_comm] = machine_action
        non_auto_states = ["standby", "override","error"]
        is_non_auto = start_state in non_auto_states
        safety = self.get_safety(hum_mvmt, mach_mvmt)
        cost = 0
        # cost for human to move
        if hum_mvmt != "none":
            cost += self.costs["human movement"]
        # cost for unsafe state
        if safety == False:
            cost += self.costs["unsafe"]
        # cost of machine updating the interface
        if mach_comm == "communicate":
            cost += self.costs["machine communication"]
        #reward for the human trying to switch to autonomous state from non-auto one
        if (is_non_auto) & (hum_comm == "pushbutton") :
            cost += self.costs["automation reward"]
        #reward for STAYING in autonomous state
        if (is_non_auto == False) & (hum_comm == "dontpushbutton"):
            cost += self.costs["automation reward"]            
        return cost


    def get_reward_string(self, start_state, human_action, machine_action):
        #Sample str: R: switch-ctrl down : loc23-rmap2-ctrlM : * : * : 95
        rew_str = "R: " + self.action_to_str(human_action) + " " + self.action_to_str(machine_action) + " : "
        rew_str += self.state_to_str(start_state) + " : * : * : "
        rew_str += str(self.get_cost(human_action,machine_action,start_state)) + "\n"
        return rew_str


    def get_observation(self,next_state,human_action, machine_action):
        [hum_mvmt, hum_comm] = human_action
        [mach_mvmt, mach_comm] = machine_action
        machine_obs = self.state_to_str(next_state)
        if (mach_comm == "communicate"): # | (hum_comm == "pushbutton"):
            human_obs = self.state_to_str(next_state)
        else:
            human_obs = "none"
        return [human_obs, machine_obs]

    def has_array_match(self, array1, array2):
        #just a helper method for the following method
        [comp1, comp2] = array2
        for elem in array1:
            [temp1, temp2] = elem
            if (temp1 == comp1) & (temp2 == comp2):
                return True
        return False

    def get_observation_string(self, start_state, human_action, machine_action):
        #sample string: O: right comm : loc31-rmap2-ctrlH : obs2 obs2: 1
        obs_str = ""
        prefix = "O: " + self.action_to_str(human_action) + " " + self.action_to_str(machine_action) + " : "
        #prefix += self.state_to_str(start_state) + " : "
        transitions = self.get_possible_transitions(start_state, human_action, machine_action)
        #[hum_mvmt, hum_comm] = human_action
        #[mach_mvmt, mach_comm] = machine_action
        #flag = False
        # if (hum_mvmt == "accel") & (hum_comm == "pushbutton") & (start_state == "following") & (mach_mvmt == "accel"):
        #     print(human_action)
        #     print(machine_action)
        #     print(transitions)
        #     flag = True
        if len(transitions) == 0:
            #state stays the same
            next_state = start_state
            [human_obs, machine_obs] = self.get_observation(next_state,human_action,machine_action)
            obs_str += prefix + self.state_to_str(next_state) + " : " + human_obs + " " + machine_obs + " : 1\n"
        else:
            explored_transitions = []
            
            for t in transitions:
                [cause, next_state] = t
                start_end_pair = [start_state, next_state]
                #this check prevents repeats if multiples of the same transition can happen from different causes
                check = self.has_array_match(explored_transitions,start_end_pair)
                if (check == False):
                    explored_transitions.append(start_end_pair)
                    #print(explored_transitions)
                    [human_obs, machine_obs] = self.get_observation(next_state,human_action,machine_action)
                    obs_str += prefix + self.state_to_str(next_state) + " : " + human_obs + " " + machine_obs + " : 1\n"
        return obs_str



    def new_trans_string(self, prefix, next_state, prob) :
        prefix += self.state_to_str(next_state) + " : " + str(prob) + "\n"
        return prefix

    def get_cost_from_start_state(self, start_state, hum_action, mach_action):
        #next_state = self.decpomdp.transition(start_state,hum_action,mach_action)
        return self.decpomdp.get_cost(hum_action,mach_action, start_state)

    def get_possible_transitions(self, start_state, hum_action, mach_action):
        #gives set of possible end states and the cause for those transitions
        transitions = []
        [hum_phys, hum_comm] = hum_action
        [mach_phys, mach_comm] = mach_action
        for row in mode_change_table:
            [starts, ends, cause] = row
            if start_state in starts:
                if cause[0] == "event":
                    #this means an event occurred
                    trans = [[cause, ends[0]]]
                    transitions += trans
                else:
                    if cause[0] == "human":
                        #this means it was a human action
                        if (cause[1] == hum_phys) | (cause[2] == hum_comm):
                            for end_state in ends:
                                trans = [[cause, end_state]]
                                transitions += trans
                    elif cause[0] == "machine":
                        #this means it was a machine action
                        if (cause[1] == mach_phys) | (cause[2] == mach_comm):
                            for end_state in ends:
                                trans = [[cause, end_state]]
                                transitions += trans
        #print("TRANSITIONS:" + str(transitions))
        return transitions

    def combine_duplicate_transitions(self, trans_table):
        #combines probabilities for transitions that end up in the same next-state
        
        prelen = len(trans_table)
        return_table = []
        
        while len(trans_table)>1:
            flag = True 
            j = 1
            while j < len(trans_table):
                if trans_table[0][0] == trans_table[j][0]:
                    #print("Duplicate Found")
                    flag = False
                    return_table += [[trans_table[0][0], trans_table[0][1]+trans_table[j][1]]]
                    trans_table.remove(trans_table[j])
                else:
                    j += 1
            if flag:
                return_table += [trans_table[0]]
            trans_table.remove(trans_table[0])
            if trans_table is None:
                trans_table = []
        return_table += trans_table
        return return_table
            

    def get_transition_table(self, state, human_action, machine_action):
        #Gets table of possible next states and their probability
        #[[state1,p1], [state2,p2],...]
        transition_table = []
        p_error = float(self.prob_dict["error"])
        p_hold_exit = float(self.prob_dict["exithold"])

        possible_transitions = self.get_possible_transitions(state, human_action, machine_action)
        if len(possible_transitions)>0:
            num_transitions = len(possible_transitions)
            remaining_prob = float(1/num_transitions)
            if (state == "following")|(state == "speedcontrol")|(state=="hold"):
                prob_error = float(p_error/num_transitions)
                num_transitions = num_transitions - 1
                if num_transitions > 0:
                    remaining_prob = float((1 - prob_error)/num_transitions)
                else:
                    remaining_prob = float((1 - prob_error))
            if state == "hold":
                prob_hold = p_hold_exit/num_transitions
                num_transitions = num_transitions - 1
                if num_transitions > 0:
                    remaining_prob = float((1 - prob_hold - prob_error)/num_transitions)
                else: 
                    remaining_prob = float((1 - prob_hold - prob_error))
            if num_transitions == 0:
                #state stays the same unless there's an event
                trans_line = [[state, remaining_prob]]
                transition_table += trans_line
            for transition in possible_transitions:
                [cause, end_state] = transition
                if cause[1] == "error":
                    trans_line = [[end_state, prob_error] ]
                elif cause[1] == "exit": 
                    trans_line = [[end_state, prob_hold]]
                else:
                    trans_line = [[end_state, remaining_prob]]
                transition_table += trans_line
        else:
            #state stays the same
            trans_line = [[state,float(1)]]
            transition_table += trans_line
        return self.combine_duplicate_transitions(transition_table)
                                            

    def get_observation_probabilities(self, state, human_action, machine_action):
        #given a start state and actions, what possible things could I observe with what likelihood
        possible_transitions = self.get_transition_table(state, human_action, machine_action)
        for elem in possible_transitions:
            [next_state, probability] = elem
            [human_obs, machine_obs] = self.get_observation(next_state, human_action, machine_action)
            print("Next state: " + next_state)
            print("--> Human will observe " + human_obs + " with " + str(round(100*probability,2)) + "%% likelihood")
            print("--> Machine will observe " + machine_obs + " with " + str(round(100*probability,2)) + "%% likelihood")
            
    def get_possible_observations(self, state, human_action, machine_action):
        #returns a list of all possible observations for human and machine [human_obs_list, machine_obs_list]
        human_obs_list = []
        mach_obs_list = []
        possible_transitions = self.get_transition_table(state, human_action, machine_action)
        for elem in possible_transitions:
            [next_state, probability] = elem
            [human_obs, machine_obs] = self.get_observation(next_state, human_action, machine_action)
            human_obs_list.append(human_obs)
            mach_obs_list.append(machine_obs)
        return [human_obs_list, mach_obs_list]
    
    def get_possible_next_states(self, state, human_action, machine_action):
        possible_transitions = self.get_transition_table(state, human_action, machine_action)
        next_states = []
        for elem in possible_transitions:
            [next_state, probability] = elem
            next_states.append(next_state)
        return next_states

    def get_transition_strings(self, state, human_action, machine_action):
        #Gets Transition strings for the LARGE ACC Model
        #T: right right : loc23-rmap2-ctrlM : loc23-rmap1-ctrlM : .1
        transition_list = []
        prefix = "T: " + self.action_to_str(human_action) + " " + self.action_to_str(machine_action) + " : "
        prefix += self.state_to_str(state) + " : "
        transition_table = self.get_transition_table(state, human_action, machine_action)
        for elem in transition_table:
            [end_state, prob] = elem
            transition_list += prefix  + self.state_to_str(end_state) + " : " + str(prob) + "\n"
        return transition_list
        


    def get_transitions(self):
        transitions = []
        observations = []
        rewards = []
        for state in self.states:
            if state != "sink":
                m_actions = self.get_allowed_machine_actions(state)
                m_actions2 = self.get_unallowed_machine_actions(state)
                for h_action in self.human_actions:
                    for m_action in m_actions:
                        transitions += self.get_transition_strings(state,h_action,m_action)
                        observations.append(self.get_observation_string(state,h_action,m_action))
                        rewards.append(self.get_reward_string(state,h_action,m_action))
                    for m_action in m_actions2:
                        transitions += "T: " + self.action_to_str(h_action) + " " + self.action_to_str(m_action) + " : " + self.state_to_str(state) + " : sink : 1\n"     
                        rwd = "R: " + self.action_to_str(h_action) + " " + self.action_to_str(m_action) + " : " + self.state_to_str(state) + " : * : * : -100000\n"
                        rewards.append(rwd)
        transitions += "T: * * : sink : sink : 1 \n"
        observations += "O: * * : sink : none sink : 1\n"
        return [transitions, observations, rewards]

    def make_decpomdp(self, start_state):
        [transitions, observations, rewards] = self.get_transitions()
        t_string = ''.join(transitions) 
        #t_string = t_string.replace(' ', '')
        t_string = t_string.split("\n")
        for elem in t_string:
            t_list = elem.split(':')
            if len(t_list) >= 6:
                actions = t_list[1].split(' ')
                entry = [actions[1].split("-"), actions[2].split("-"), t_list[2].replace(' ',''), t_list[4].replace(' ',''), float(t_list[5])]
                print(entry)

    
    def get_graph_viz_limit_branches(self, human_tree, machine_tree, start_state):
        #returns trees in graph_viz format including only relevant branches
        #ONLY WRITTEN FOR TREES OF HEIGHT 1 FOR NOW
        output1 = 'digraph human_tree {\n'
        output2 = 'digraph machine_tree {\n'
        output1 += 'edge [dir=none];\n'
        output2 += 'edge [dir=none];\n'
        nodes_h = ""
        edges_h = ""
        nodes_m = ""
        edges_m = ""
        output1 += 'node0 [ label = "' + self.action_to_str(human_tree.nodes[0]) + '" ];\n'
        output2 += 'node0 [ label = "' + self.action_to_str(machine_tree.nodes[0]) + '" ];\n'
        [human_obs, mach_obs] = self.get_possible_observations(start_state, human_tree.nodes[0], machine_tree.nodes[0])
        num_hum_nodes = 1
        num_mach_nodes = 1
        for i in range(1,len(human_tree.nodes)):
            human_edge = human_tree.edges[i]
            machine_edge = machine_tree.edges[i]
            if human_edge in human_obs:
                nodes_h += 'node' + str(num_hum_nodes) + ' [ label = "' + self.action_to_str(human_tree.nodes[i]) + '" ];\n'
                edges_h += 'node0 -> ' 
                edges_h += 'node' + str(num_hum_nodes) + ' [label="' + str(human_tree.edges[i]) + '"];\n'
                num_hum_nodes += 1
            if machine_edge in mach_obs:
                nodes_m += 'node' + str(num_mach_nodes) + ' [ label = "' + self.action_to_str(machine_tree.nodes[i]) + '" ];\n'
                edges_m += 'node0 -> ' 
                edges_m += 'node' + str(num_mach_nodes) + ' [label="' + str(machine_tree.edges[i]) + '"];\n'
                num_mach_nodes += 1
        output1 += nodes_h + edges_h
        output2 += nodes_m + edges_m
        output = [output1 + '}', output2 + '}']
        return output
    
    def write_to_file(self, filename, start_state):
        file_data = []
        file_data.append("agents: 2" + "\n")
        file_data.append("discount: 1" + "\n")
        file_data.append("values: reward" + "\n")
        file_data.append(self.all_states_to_str() + "\n")
        start_str = "start include: " + self.state_to_str(start_state) + "\n"
        file_data.append(start_str)
        file_data.append("actions:\n")
        file_data.append(self.action_list_to_str(self.human_actions) + "\n")
        file_data.append(self.action_list_to_str(self.machine_actions) + "\n")
        file_data.append("observations:\n")
        file_data.append(self.list_to_str(self.human_observations) + "\n")
        file_data.append(self.list_to_str(self.machine_observations) + "\n")
        [transitions, observations, rewards] = self.get_transitions()
        file_data += transitions
        file_data += observations
        file_data += rewards
        #print(file_data)
        f = open(filename, "w")
        f.writelines(file_data)
        f.close()
