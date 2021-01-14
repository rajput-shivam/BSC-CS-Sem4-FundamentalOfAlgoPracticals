#BFS

def bfs(graph, source, dest):
  visited, queue = [source], [source] 
  while queue:                  
    s = queue.pop(0)
    print(s, end = " ")
    if s == dest:
      return "\nRecahed Destination"
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

graph = {
    'Arad' : ['Timisoara', 'Sibia', 'Zaerind'],
    'Timisoara' : ['Arad','Lugoj'],
    'Sibia' : ['Arad','Sibui', 'Fagaras'],
    'Zaerind' : ['Arad','Orudea'],
    'Lugoj' : ['Timisoara'],
    'Sibui' : ['Sibia'],
    'Fagaras' : ['Sibia','Bucharest'],
    'Orudea' : ['Zaerind','Bucharest'],
    'Bucharest' : ['Fagaras', 'Orudea']
}
source = 'Arad'
dest = 'Bucharest'
print(bfs(graph, source, dest))


