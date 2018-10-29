inf=9999999999
# graph1=[ [0,10,3,inf,inf],[inf,0,1,2,inf],[inf,4,0,8,inf],[inf,inf,inf,0,7],[inf,inf,inf,9,0]]
def criaVertice ():
	graph=[]
	nVertice = int(input("Digite o número de vértices: "))
	for x in range(0,nVertice):
		aux = []
		for  y in range(0,nVertice):
			if(x==y):
				aux.append(0)
			else:
				c = input("Existe arestas de "+str(x)+" e "+str(y)+"(s/n): ")
				if c == 'n':
					aux.append(inf)
				else:
					peso = int(input("Digite o peso de "+str(x)+" e "+str(y)+": "))
					aux.append(peso)
		graph.append(aux)
	return graph


def FloydWarshal(graph):
	n = len(graph)
	
	pred = [] 
	for x in range(0,n):
		aux=[]
		for y in range(0,n):
			aux.append(x)
		pred.append(aux)			
			
	for k in range(0,n):
		for i in range(0,n):
			for j in range(0,n):
				if graph[i][j]> graph[i][k]+graph[k][j]:	
					graph[i][j]=graph[i][k]+graph[k][j]
					pred[i][j]=pred[k][j]
	print("Matriz de predecessor")				
	print(pred)
	print("Matriz de caminho mínimo")
	print(graph)
	return graph

FloydWarshal(criaVertice())			
