class Vertex:
	"""docstring for Vertex"""
	def __init__(self,name,dist,pred):
		self.name=name
		self.dist = dist
		self.pred = pred 
		
# a = Vertex('a','NULL','NULL')
# b = Vertex('b','NULL','NULL')
# c = Vertex('c','NULL','NULL')
# d = Vertex('d','NULL','NULL')
# e = Vertex('e','NULL','NULL')
# graph2 = {a:{b:10,c:3},b:{c:1,d:2},c:{b:4,d:8},d:{e:7},e:{d:9}}
graph={}

def criaVertice ():
	aux = {}
	nVertice = int(input("Digite o número de vertice: "))
	for x in range(0,nVertice):
		nome = input("Digite o nome do vertice: ")
		nome = Vertex(nome,'NULL','NULL')
		graph[nome] = aux
		
	for x in graph:
		aux = {}
		nArestas = int(input("Número de arestas de "+x.name+": "))	
		for y in range(0,nArestas):
			auxNome = input("Digite os adjacentes de "+x.name+": ")
			for k in graph:
				if auxNome == k.name:
					auxNome = k
			peso= int(input("Digite o peso: "))
			aux[auxNome] = peso	
		graph[x] = aux

	return graph



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

def verificaCaminho(s,v):
	while v.pred!=None:
		if v.pred==s:
			return True
		v=v.pred	
	return False

def escolheAlgoritimo(graph):
	print("1 - dijkstra")
	print("2 - BellmanFord")
	n = int(input("Digite qual Algoritimo usar: "))
	if n == 1:
		s = input("Digite o vértice inicial: ")
		for k in graph:
			if s == k.name:
				s = k
		dijkstra(graph,s)
		v = input("Digite o vértice final: ")
		for k in graph:
			if v == k.name:
				v = k
		if verificaCaminho(s,v):
			caminhoMinimo(v)
		else:
			print("Não há caminho para o vértice")
	if n == 2:
		s = input("Digite o vértice inicial: ")
		for k in graph:
			if s == k.name:
				s = k
		BellmanFord(graph,s)
		v = input("Digite o vértice final: ")
		for k in graph:
			if v == k.name:
				v = k		
		if verificaCaminho(s,v):
			caminhoMinimo(v)
		else:
			print("Não há caminho para o vértice")


escolheAlgoritimo(criaVertice())
