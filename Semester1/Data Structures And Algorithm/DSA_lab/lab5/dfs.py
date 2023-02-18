adj_list = {
    "0": ["1", "2"],   
    "1": ["0", "3", "4"],  
    "2": ["0"],
    "3": ["1"],
    "4": ["2","3"],
}

color = {}    
parent = {}  
dfs_traversal_order = [] 

for node in adj_list.keys():
    color[node] = "W"
    parent[node]= None

def dfs_util(u): 
    color[u] =  "G"
    dfs_traversal_order.append(u)
    
    for v in adj_list[u]:
        if color[v] == "W": 
            parent[v] = u 
            dfs_util(v)
    color[u] = "B" 
    

dfs_util("0")
print("dfs_traversal_order :")
print(dfs_traversal_order)

v = "2"
path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print("Path: ")
print(path)