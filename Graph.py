from collections import defaultdict
import matplotlib.pyplot as plt

class Graph:

    def __init__(self,num):
        self.vertices = num
        self.edges = 0
        self.nodes = defaultdict(set)
        for i in range(self.vertices):
            self.nodes[i]


    def add_edge(self,l :int, r :int):
        self.edges += 1
        if not l in self.nodes[r]:
            self.nodes[r].add(l)

        if not r in self.nodes[l]:
            self.nodes[l].add(r)

    def degree_of(self,i):
        return len(self.nodes[i])
    
    def print(self):
        for k,v in self.nodes.items():
            print(k,v)

    def DFS(self, node, visited):
        stack = []

        stack.append(node)

        while len(stack) > 0:
            s = stack.pop()
            if not visited[s]:
                visited[s] = True
            for i in self.nodes[s]:
                if not visited[i]:
                    stack.append(i)
                    
##        visited[node] = True
##        for i in self.nodes[node]:
##            if not visited[i]:
##                self.DFS(i,visited)
                
    def connected_components(self):
        visited = [False] * self.vertices
        num = 0
        
        for i in self.nodes.keys():
            if not visited[i]:
                self.DFS(i,visited)
                num += 1                

        return num

    def get_degrees(self):
       d = defaultdict(int) 
       for i in range(self.vertices):
           d[self.degree_of(i)] += 1
       return d 

                
def open_file_and_compute_components():
    file = open(input("Enter a file name : ")).readlines()
    num = int(file[0])
    list_of_tuples = file[1:]

    g = Graph(num)
    
    for i in list_of_tuples:
        k,v = map(int, i.split())
        g.add_edge(k,v)

    g.print()
    print("Number of connected components :", g.connected_components())
    myDictionary = g.get_degrees()

##    plt.xlabel('Degrees')
##    plt.ylabel('# of Nodes')
##    plt.title('Histogram of Degree distribution')
##    plt.bar(list(myDictionary.keys()), list(myDictionary.values()),color='b')
##    plt.show()


while True:
    i = input("Choose from the two options\n1: To add a file for processing\n2: To quit the program\nOption : ")
    if i == '1':
        open_file_and_compute_components()
        print()
    elif i == '2':
        print("Bye :(")
        break
    else:
        print("Type probably dummy!")

