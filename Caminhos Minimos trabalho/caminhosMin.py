class Vertex:
	"""docstring for Vertex"""
	def __init__(self,name,dist,pred):
		self.name=name
		self.dist = dist
		self.pred = pred 
		
a = Vertex('a','NULL','NULL')
b = Vertex('b','NULL','NULL')
c = Vertex('c','NULL','NULL')
d = Vertex('d','NULL','NULL')
e = Vertex('e','NULL','NULL')


graph = {a:{b:10,c:3},b:{d:2,c:1},c:{b:4,d:8},d:{e:7},e:{d:9}}

def Inicialize (graph,s):
	for x in graph:
		x.dist = 9999999999999999
		x.pred = None
	s.dist = 0

def relax(u,v,peso):
	if (v.dist>u.dist+peso):
		v.dist=u.dist+peso
		v.pred = u

def  Extract_min(Q):
	aux = Q[0]
	for x in Q:
		 if aux.dist>x.dist:
		 	aux = x
	Q.remove(aux)	 
	return aux

def dijkstra (graph,s):
	Inicialize(graph,s)
	ListS = []
	ListQ = []
	for x in graph:
		ListQ.append(x)

	while ListQ!=[]:
		u = Extract_min(ListQ)
		for x in graph[u]:
			ListS.append(x)
		for x in ListS: 
			relax(u,x,graph[u][x])
		ListS = []	

	
def BellmanFord(graph,s):
	Inicialize(graph,s)
	ListQ = []
	for x in graph:
		ListQ.append(x)

	for x in (1,len(ListQ)-1):
		for i in graph:
			for j in graph[i]:
				relax(i,j,graph[i][j])
	for i in graph:
			for j in graph[i]:
				if(j.dist>i.dist+graph[i][j]):
					return False
			return True
				
				

		
def caminhoMinimo(v):
	print(v.name)
	if(v.pred!=None):
		caminhoMinimo(v.pred)

BellmanFord(graph,a)
if BellmanFord:
	print("NÃO TEM CICLO NEGATIVO")
else:
	print("Tem ciclo negativo")

print("Caminho mínime até o vértice: "+e.name)
caminhoMinimo(e)
