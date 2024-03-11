#Given a reference of a node in a connected undirected graph.

#Return a deep copy (clone) of the graph.

#Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

#class Node {
#    public int val;
#    public List<Node> neighbors;
#}



#python3 solution: 

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None): 
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

#note that neighbors = None is specified above!
#The val parameter is the value associated with the node. It has a default value of 0.
#The neighbors parameter is used to specify the neighboring nodes of the current node. If neighbors is provided during the initialization of a Node object, it will be assigned to the neighbors attribute. Otherwise, if neighbors is None, an empty list [] will be assigned to self.neighbors.
#So, when a Node object is created, you have the option to specify its value (val) and its neighboring nodes (neighbors). If no neighboring nodes are specified during initialization, an empty list will be assigned by default.

#val attribute is also provided above
#The val attribute represents the value associated with a node. It's essentially any data you want to associate with that node. For example, in a graph representing cities and their populations, val might represent the population of a city.
#When you create a new Node object, you can specify the value for that node by passing it as an argument to the val parameter during initialization. If you don't provide a value, it defaults to 0.
#When a Node object is created, its val attribute will be assigned the value provided during initialization.
#For example, if you create a Node object like this: node1 = Node(5). Here, node1 will have a val attribute with the value 5
#You can access the value of a Node object using the dot notation. For example: print(node1.val)  # Output will be 5 - This will print the value associated with node1, which is 5.

#The line from typing import Optional is a Python import statement that imports the Optional type hint from the typing module.

#In Python, type hints are used to indicate the expected types of function arguments and return values. They are not enforced by the Python interpreter at runtime but can be used by static type checkers or IDEs to provide type checking and code analysis.

#The Optional type hint from the typing module is used to indicate that a particular argument or return value can be of a certain type or None. For example, Optional[int] indicates that the value can be an integer or None.

#In the provided code snippet, Optional['Node'] indicates that the function cloneGraph takes an argument named node, which can be either a Node object or None. Similarly, Optional['Node'] as the return type indicates that the function can return either a Node object or None.
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #dfs approach
        mydict = {} #stores original nodes: cloned nodes
        def f(node): #helper function performs cloning recursively - it takes a node from the original graph as input and returns the corresponding cloned node
            if node in mydict: #clone has already been created, so return corresponding cloned node from the dictionary
                return mydict[node]
            copy = Node(node.val) #input node is not in mydict, so create a new node with the same value as the original node and add it to mydict
            mydict[node] = copy #adding copy to mydict
            for n in node.neighbors: #iterate through neighbors of the original node recursively, cloning each neighbor and adding the clone to the neighbors list of the cloned node
                copy.neighbors.append(f(n))
            return copy #returns cloned node corresponding to the original node
        return f(node) if node else None #entrypoint of recursive function. starts cloning from the given input node. If inputnode is None, it returns None because there's no graph to clone. 


#the dictionary mydict is used to ensure that each node is only cloned once, 
#preventing infinite recursion in cases where nodes reference each other cyclically. 
#The key is the original node, and the value is the corresponding cloned node. 
#This dictionary is consulted before cloning a node to see if it has already been cloned, and if so, the previously cloned version is returned.

#3/8/24:

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mydict = {}
        def f(node):
            if node in mydict:
                return mydict[node]
            copy = Node(node.val)
            mydict[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(f(n))
            return copy
        return f(node) if node else None


#3/9/24:

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None): 
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mydict = {} #original:copy
        def f(node):
            if node in mydict:
                return mydict[node]
            copy = Node(node.val)
            mydict[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(f(n))
            return copy
        
        return f(node) if node else None



#3/10/24:

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None): 
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mydict = {}
        def f(node):
            if node in mydict:
                return mydict[node]
            copy = Node(node.val)
            mydict[node] = copy #node is the original node itself that was passed as input from the very beginning of the recursion 
            for n in node.neighbors:
                copy.neighbors.append(f(n))
            return copy
        return f(node) if node else None


#3/11/24:

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mydict = {}
        def f(node):
            if node in mydict:
                return mydict[node]
            copy = Node(node.val)
            mydict[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(f(n)) #creating the edges between nodes in the cloned graph - When n is node2, f(n) will create copy2. copy1.neighbors.append(copy2) will connect copy1 to copy2.
            return copy
        return f(node) if node else None

#Explanation of copy.neighbors.append(f(n)):

Initial state:
  Original Graph           Cloned Graph
  --------------           -------------
  Node 1 -> Node 2        copy1 -> copy2
    |         |              |        |
    v         v              v        v
  Node 4 <- Node 3        copy4 <- copy3

After executing `copy.neighbors.append(f(n))` for each neighbor of node1:

  copy1.neighbors = [copy2, copy4]
