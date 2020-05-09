def rules():
    input_rules = open("rules.txt")
    rules_dict = dict()
    for entry in input_rules:
        [non_term, prod] = [i.strip() for i in entry.split("->")]
        prod = prod.split(" ")
        if non_term not in rules_dict:
            rules_dict[non_term]=[]
        rules_dict[non_term].append([non_term]+prod)
    return rules_dict

def predict(state, k):
    for rule in rules_dict[state[0][state[1]]]:
        if (rule,1,k) not in state_sets[k]:
            state_sets[k].append((rule,1,k))
def scan(state,k, max):
    if k!=max and state[0][state[1]] == words[k]:
        if (state[0],state[1]+1,state[2]) not in state_sets[k+1]:
            state_sets[k+1].append((state[0],state[1]+1,state[2]))
def complete(state, k):
    for state2 in state_sets[state[2]]:
        if state2[1] != len(state2[0]) and state2[0][state2[1]]==state[0][0]:
            state_sets[k].append((state2[0],state2[1]+1,state2[2]))

rules_dict = rules()
non_terms =['N','VP','S','V','PP','P','NP']
sentence = "they can fish in rivers"
words = sentence.split(" ")
state_sets = [[] for _ in range(len(words)+1)]
state_sets[0].append((rules_dict['S'][0], 1, 0))
for k in range(len(words)+1):
    for state in state_sets[k]:
        if not state[1]==len(state[0]):
            if(state[0][state[1]] in non_terms):
                predict(state,k)
            else:
                scan(state,k,len(words))
        else:
            complete(state,k)

for i in state_sets[len(words)]:
    if i == (['S','NP','VP'],3,0):
        print(i)


