from queue import Queue
adj_list = {
    "0": ["1", "2"],   
    "1": ["0", "3", "4"],  
    "2": ["0"],
    "3": ["1"],
    "4": ["2","3"],
}

visited = {}    # dict
parent = {}
bfs_traversal_order =[]  # lst
queue = Queue()   

for node in adj_list.keys():
    visited[node] = False  
    parent[node] = None  
s = "0" 
visited[s] = True  
queue.put(s)  


while not queue.empty():
    u = queue.get()  
    bfs_traversal_order.append(u)      
    for v in adj_list[u]:   
        if not visited[v]:        
            visited[v] = True       
            parent[v] = u            
            queue.put(v)            
            
print("BFS Traversal Order  : ")
print(bfs_traversal_order)           

destination = "4"
path = []
while destination is not None:
    path.append(destination)
    destination = parent[destination]
path.reverse()
print("Path : ")
print(path)