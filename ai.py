import copy 



class State:
  def __init__(self, A, cost, parent, deep):
    self.A = A
    self.cost = cost
    self.parent = parent
    self.deep = deep


def min_cost(explored):
	minimum = -1
	index=0
	for i in range(0,len(explored)):
		k = explored[i].cost	
		if k < minimum or minimum == -1:
			minimum = k
			index = i
	return explored[index]


def max_depth(explored):
	max_dept = -1
	index=0
	for i in range(0,len(explored)):
		k = explored[i].deep	
		if k > max_dept or max_dept == -1:
			max_dept = k
			index = i
	return explored[index]	



def is_small(state, target, value):

	for i in state.A[0]:
		if 0 == target:
			break
		if value < i:
			return True	

	for i in state.A[1]:
		if 1 == target:
			break
		if value < i:	
			return True

	for i in state.A[2]:
		if 2 == target:
			break
		if value < i:	
			return True

	return False		

def calculate_cost(state, target, i):
	cost = 0
	rod = len(state.A[0]) + len(state.A[1]) + len(state.A[2])

	x = rod - len(state.A[target]) 
	y = 0

	for j in state.A[target]:
		if is_small(state, target, j):
			y += 1	
	#print(state.A, x + 2*y + state.deep)
	return x + 2*y + state.deep		


def expand(parent, target, i):
	temp  = copy.deepcopy(parent)
	temp2 = copy.deepcopy(parent)
	temp3 = copy.deepcopy(parent)
	temp4 = copy.deepcopy(parent)
	temp5 = copy.deepcopy(parent)
	temp6 = copy.deepcopy(parent)
	#print(temp3.A)
	liste = []
	#A->B
	if temp.A[0] != [] and ( (temp.A[1] == [])	or (temp.A[0][-1] < temp.A[1][-1]) ):
		change = temp.A[0][-1]
		temp.A[0].pop()
		temp.A[1].append(change)
		
		new1 = State( temp.A, 0, parent, parent.deep + 1)
		cost = calculate_cost(new1, target, i)
		new1.cost = cost
		liste.append(new1)
	#A->C	
	
	if temp2.A[0] != [] and ( (temp2.A[2] == [])	or (temp2.A[0][-1] < temp2.A[2][-1]) ):
		change = temp2.A[0][-1]
		temp2.A[0].pop()
		temp2.A[2].append(change)
		
		new2 = State( temp2.A, 0, parent, parent.deep + 1)
		cost = calculate_cost(new2, target, i)
		new2.cost = cost	
		liste.append(new2)
	#B->A	
	
	if temp3.A[1] != [] and ( (temp3.A[0] == [])	or (temp3.A[1][-1] < temp3.A[0][-1]) ):
		change = temp3.A[1][-1]
		temp3.A[1].pop()
		temp3.A[0].append(change)
		
		new3 = State( temp3.A, 0, parent, parent.deep + 1)
		cost = calculate_cost(new3, target, i)
		new3.cost = cost
		liste.append(new3)
	#B->C
	if temp4.A[1] != [] and ( (temp4.A[2] == [])	or (temp4.A[1][-1] < temp4.A[2][-1]) ):
		change = temp4.A[1][-1]
		temp4.A[1].pop()
		temp4.A[2].append(change)
			
		new4 = State( temp4.A, 0, parent, parent.deep + 1)
		cost = calculate_cost(new4, target, i)
		new4.cost = cost
		liste.append(new4)
	#C->A
	
	if temp5.A[2] != [] and ( (temp5.A[0] == [])	or (temp5.A[2][-1] < temp5.A[0][-1]) ):
		change = temp5.A[2][-1]
		temp5.A[2].pop()
		temp5.A[0].append(change)

		new5 = State( temp5.A, 0, parent, parent.deep + 1)
		cost = calculate_cost(new5, target, i)
		new5.cost = cost	
		liste.append(new5)
	#C->B		
	if temp6.A[2] != [] and ( (temp6.A[1] == [])	or (temp6.A[2][-1] < temp6.A[1][-1]) ):
		change = temp6.A[2][-1]
		temp6.A[2].pop()
		temp6.A[1].append(change)

		new6 = State( temp6.A, 0, parent, parent.deep + 1)
		cost = calculate_cost(new6, target, i)
		new6.cost = cost	
		liste.append(new6)

	return liste	



def state_equal(n, lst):
	for i in range(0,len(lst)):
		if lst[i].A == n.A:
			return i
	return -1		


def A_star_search(initial_state, target, goal_state, limit_cost, flag):
	explored = [initial_state]
	visited = []
	costly = []
	i = 1
	while 1:

		if explored == [] and flag == 0:
			print("FAILURE")
			return None

		if explored == [] and flag == 1:
			return min_cost(costly)

		if flag == 0:
			state = min_cost(explored)
		if flag == 1:
			state = max_depth(explored)
		#print(state.A,state.cost, state.deep)
		
		explored.remove(state)
		visited.append(state)	

		if state.A == goal_state.A:
			return state
		#print(state.A,"expand")
		expand_list = expand(state, target, i)	
		i += 1

		for n in expand_list:
			#print("-",n.A,n.cost,n.deep,"-")
			temp = state_equal(n,explored)
			temp2 = state_equal(n,visited)
			
			if temp == -1 and temp2 == -1:
				if n.cost <= limit_cost:
					explored.append(n)
				else:
					costly.append(n)
					#print(n.A,n.cost)				
			
			elif temp != -1 and n.cost < explored[temp].cost:
				explored[temp] = copy.deepcopy(n) 

			elif temp2 != -1 and n.cost < visited[temp2].cost:
				explored.append(n)	





def IDA_A_star(initial_state, target, goal_state, limit_cost):

	f_max = inital_state.cost
	while 1:
		
		temp = A_star_search(inital_state, target, goal_state, f_max, 1)
		#print("--",temp.A, temp.cost)
		if temp.A == goal_state.A:
			return temp
		elif temp.cost <= limit_cost:
			f_max = temp.cost
		else:
			print("FAILURE")
			return None	
				


def print_solution(new_state):
	ls = []
	while new_state != None:
		#print(new_state.A)
		ls.append(new_state.A)
		new_state = new_state.parent
	print("SUCCESS\n")
	for i in range(0,len(ls)):
		#txt = "A - >{}\t B - >{}\t C - >{}\n".format(ls[len(ls)-i-1][0], ls[len(ls)-i-1][1], ls[len(ls)-i-1][2] )
		if i == len(ls) - 1:
			print("A->" + str(ls[len(ls)-i-1][0])+ "\t" + "B->" + str(ls[len(ls)-i-1][1])+ "\t" + "C->" + str(ls[len(ls)-i-1][2]) + "\n")
			break		
		print("A->" + str(ls[len(ls)-i-1][0]) + "\t" + "B->" + str(ls[len(ls)-i-1][1])+ "\t" + "C->" + str(ls[len(ls)-i-1][2]) + "\n\n")
		#print(ls[len(ls)-i])
		#print(txt)



Method = input()
M = input()
N = input()
T = input()

lst = []
lst.append(list(input()))
lst.append(list(input()))
lst.append(list(input()))

if Method == "A*":
	funciton = 0

if Method == "IDA*":
	funciton = 1	

if T == "A":
	target = 0
if T == "B":
	target = 1
if T == "C":
	target = 2		


lst2 = [[],[],[]]
goal = []

if len(lst[0]) != 0:
	for i in lst[0]:
		if i != ",":
			lst2[0].append(int(i))
			goal.append(int(i))

if len(lst[1]) != 0:
	for i in lst[1]:
		if i != ",":
			lst2[1].append(int(i))
			goal.append(int(i))

if len(lst[2]) != 0:
	for i in lst[2]:
		if i != ",":
			lst2[2].append(int(i))		
			goal.append(int(i))				


goal.sort(reverse=True)
goal_lst = [[],[],[]]
goal_lst[target] = goal

inital_state = State([lst2[0],lst2[1],lst2[2]], 0, None, 0)

goal_state = State(goal_lst, 0, None, 0)

#print(inital_state.A)
#print(goal_state.A)

if funciton == 0:
	new_state = A_star_search(inital_state, target, goal_state, int(M), 0)
if funciton == 1:
	new_state = IDA_A_star(inital_state, target, goal_state, int(M))

if new_state != None:
	print_solution(new_state)

