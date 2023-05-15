# Segundo problema de DAA

### Integrantes:

* Leonardo Ulloa Ferrer

* Roxana Peña Mendieta

### Descripcion del problema

<div>
<center><h4>Lázaro Presidente del PCC</h4></center>
</div>

Han pasado 20 años desde que Lázaro se graduó de Ciencias de la Computación (haciendo una muy buena tesis) y las vueltas de la vida lo llevaron a convertirse en el presidente del Partido Comunista de Cuba. Una de sus muchas responsabilidades consiste en visitar zonas remotas. En esta ocasión debe visitar una ciudad campestre de Pinar del Río.  

También han pasado 20 años desde que Marié consiguió su título en MAT- COM. Tras años de viaje por las grandes metrópolis del mundo, en algún punto  decidió que prefería vivir una vida tranquila, aislada de la urbanización, en una  tranquila ciudad de Pinar del Río. Las vueltas de la vida quisieron que precisamente Marié fuera la única iniversitaria habitando la ciudad que Lázaro se dispone a visitar. Los habitantes de la zona entraron en pánico ante la visita de una figura tan importante y decidieron reparar las calles de la ciudad por las que transitaría  Lázaro. El problema está en que nadie sabía qué ruta tomaría el presidente y  decidieron pedirle ayuda a Marié. La ciudad tiene n puntos importantes, unidos entre sí por calles cuyos  tamaños se conoce. Se sabe que Lázaro comenzará en alguno de esos puntos (s) y terminará el viaje en otro (t). Los ciudadanos quieren saber, para cada par s, t, cuántas calles participan en algún camino de distancia mínima entre s y t.

### La idea de la solución

La solución se basa en la propiedad de que el conjunto de las aristas que participan en un camino de costo mínimo de $s$ a $t$, es igual a la intercepción del conjunto de las aritstas que participan en algún camino de costo mínimo que parte de $s$, con el conjunto de las aristas donde el vértice más lejano a $s$, de los dos vértices que relaciona, pertenece a un camino de costo mínimo de $s$ a $t$. 

Luego para calcular las aristas que participan en algún camino de costo mínimo que parte de $s$ usamos la propiedad de que una arista $<u,v>$ con $\delta(s,u) < \delta(s,v)$ cumple esto ssi $\delta(s,v) = \delta(s,u) + w(<u,v>)$

Para calcular los vértices que participan en un camino de costo mínimo de $s$ a $t$ usamos la propiedad de que un vértice $v$ cumple esto ssi $\delta(s,t) = \delta(s,v) + \delta(v,t)$

Luego se puede utilizar el algoritmo de dijkstra para calcular, para cada punto importante, los caminos de costo mínimo y la aristas que participen en algunos de estos caminos. Para esto vamos a asignarle un array de tamaño $|V|$ a cada vértice $v$, donde almacenaremos en el índice $i$ la cantidad de aristas que cumplen que: 

- participan en un camino de costo mínimo que parte de $V_i$ 

- de los dos vértices que relaciona la arista el más lejano a $V_i$ es $v$

Los valores de este array los calcularemos aprovechando el relax que necesita hacer dijkstra, haciendo incrimentar el valor de la posición $i$ si da igual y asignandole 1 si da menor.

Teniendo calculado esto se puede resolver en O($|V|$) las aristas que participan en un camino de costo mínimo de $s$ a $t$ acumulando lo que tiene cada vertice que participa en un camino de costo mínimo de $s$ a $t$ en su array en la posición correspondiente a $s$. Por lo que iterando por cada posible origen y final y haciendo lo anterior se puede resolver esto en O($|V|^3$) y hacer $|V|$ dijkstras es O($|V|^3$) también por lo que la solución quedaría O($|V|^3$)

### El algoritmo

```python
def optimal_solver(graph:Graph,principal_vertex:list[Vertex]): 
    # array bidimensional en el que se van a almacenar la respuesta
    edges_matrix = [[0]*len(principal_vertex) for _ in principal_vertex]
    # array de distancias
    distances_matrix = [[0]*len(graph.vertex) for _ in graph.vertex]
    for vertex in graph.vertex:
        # artributo en la que se van a almacenar las aristas 
        # que participan en un camino de costo mínimo que parte
        # desde alguno de los vértices principales
        vertex.min_edges = [0]*len(principal_vertex)

    for vertex_ind, vertex in enumerate(principal_vertex):
        # aquí además de resolver las distancias de los caminos de 
        # costo mínimo que parten de vertex también se calculan 
        # los valores de min_edge de cada vértice correspondientes a 
        # vertex
        distances_matrix[vertex.Id] = dijkstra_modificado(graph, vertex,vertex_ind)


    # Por cada combinacion de principal vertex se acumula el valor
    # de min_edges de los vertices que participan en algun camino 
    # de costo mínimo de ese par
    for ind_u in range(len(principal_vertex)):
        u = principal_vertex[ind_u]
        for ind_v in range(ind_u + 1, len(principal_vertex)):
            v = principal_vertex[ind_v]
            edges_count = v.min_edges[ind_u]
            for w in graph.vertex:
                if u == w or v == w: continue
                if distances_matrix[u.Id][w.Id] + distances_matrix[v.Id][w.Id] == distances_matrix[u.Id][v.Id]:
                    edges_count += w.min_edges[ind_u]
            edges_matrix[ind_u][ind_v] = edges_count
    return distances_matrix, edges_matrix
```

La implementación del Dijkstra Modificado

```python
def dijkstra_modificado(graph:Graph, start:Vertex,start_ind):
    distances = [float('inf') for _ in graph.vertex]
    distances[start.Id] = 0
    visited = [False] * len(graph.vertex)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if visited[current_vertex.Id]:
            continue

        visited[current_vertex.Id] = True

        for neighbor, weight  in current_vertex.neighbourhood:
            distance = current_distance + weight

            if distance < distances[neighbor.Id]:
                # En el caso de dar menor todas 
                # las aristas que se habían contando anteriormente 
                # dejan de tener valor y se cuenta la arista 
                # responsable de este relax      
                distances[neighbor.Id] = distance   
                neighbor.min_edges[start_ind] = 1
                heapq.heappush(priority_queue, (distance, neighbor))
            elif distance == distances[neighbor.Id]:
                # En caso de que de igual se suma esta arista al conjunto de las aristas que pertenecen a min_edge
                neighbor.min_edges[start_ind] += 1 
    return distances
```

### Demostración de la Correctitud

**Propiedad 1** :el conjunto de las aristas que participan en un camino de costo mínimo de $s$ a $t$, es igual a la intercepción del conjunto de las aritstas que participan en algún camino de costo mínimo que parte de $s$, con el conjunto de las aristas donde el vértice más lejano a $s$, de los dos vértices que relaciona, pertenece a un camino de costo mínimo de $s$ a $t$.

- **Demostración**: 
  
  * ($A \sub B$) Si una arista pertenece a un camino de costo mínimo de $s$ a $t$ entonces es lógico que esta arista pertenezca a algún camino de  costo mínimo que parte de $s$ y que ambos de los vértices que relacione pertenezcan a un camino de costo mínimo de $s$ a $t$
  
  * ($B \sub A$) Luego sea $<u,v>$ una arista que pertenece a algún camino de costo mínimo de $s$, supongamos $\delta(s,u) < \delta(s,v)$  y que $v$ pertenece a algún camino de costo mínimo de $s$ a $t$. Luego sea $P$ el camino de costo mínimo de $s$ a $t$ que contiene a $v$ y sea $Q$ el camino de costo mínimo que parte de $s$ que contiene la arista $<u,v>$. Luego el subcamino de $Q$ hasta $v$ contiene la arista $<u,v>$ porque $v$ está más alejado de $s$ que $u$ y la longitud de este subcamino es igual a la longitud del subcamino hasta $v$ en $P$; por lo que al sustituir en $P$ su subcamino hasta $v$, por el subcamino hasta $v$ de $Q$ se obtiene un camino de $s$ a $t$ con la misma longitud de $P$ que contiene a $<u,v>$ por lo que pertenece a un camino de longitud mínima de $s$ a $t$ 

**Propiedad 2**: una arista $<u,v>$ con $\delta(s,u) < \delta(s,v)$ pertenece a algún camino de costo mínimo que parte de $s$ ssi $\delta(s,v) = \delta(s,u) + w(<u,v>)$ 

- **Demostración**:
  
  - ($A \Rightarrow B$) Si una arista $<u,v>$ con $\delta(s,u) < \delta(s,v)$ participa en algún camino de costo mínimo que parte de $s$, entonces sea $P$ uno de estos caminos ; su subcamino de $s$ a $v$ tiene longitud $\delta(s,v)$ y como termina con los vértices $u$ y $v$, la longitud de este camino también es igual a $\delta(s,u) + w(<u,v>)$. Por lo que $\delta(s,v) = \delta(s,u) + w(<u,v>)$ 
  
  - ($B \Rightarrow A$) Si $\delta(s,v) = \delta(s,u) + w(<u,v>)$ entonces sea $P$ un camino de longitud mínima de $s$ a $u$ y añadele al final a $v$ a travez de la arista $<u,v>$ y se tiene un camino de $s$ a $v$ con longitud $\delta(s,v)$ por lo que este camino es un camino de longitud mínima de $s$ a $v$ en el que  $<u,v>$ participa

**Propiedad 3**: Un vértice $v$ participa en un camino de costo mínimo  de $s$ a $t$ ssi $\delta(s,t) = \delta(s,v) + \delta(v,t)$ 

- **Demostración:** 
  
  - ($A \Rightarrow B$) Si un vertice participa en un camino de costo mínimo de $s$ a $t$ es evidente que se cumple que $\delta(s,t) = \delta(s,v) + \delta(v,t)$ 
  
  - ($B \Rightarrow A$) Sea $v$ un vértice que cumple $\delta(s,t) = \delta(s,v) + \delta(v,t)$ entonces sea $P$ un camino de longitud mínima de $s$ a $v$ y $Q$ un camino de longitud mínima de $v$ a $t$ entonces la concatenación de estos dos caminos es un camino de $s$ a $t$ con longitud $\delta(s,t)$ por lo que es un camino de longitud mínima de $s$ a $t$ que contiene a $v$ 

Como mencionó en la sección pasada vamos a aprovechar la ejecución del algoritmo de dijkstra desde el origen $s$ para almacenar en una posición correspondiente a $s$ de un array que tiene cada vértice $v$ un valor que se va a ir incrementando con cada relax hacia ese vértice que de igual y asignandole 1 si da menor. Al terminar la ejecución en la posición correspondiente s en el array de  cada vértice $v$ va a estar la cantidad de aristas que participan en un camino de costo mínimo que parte desde $s$ que cumplen que su vertice más lejano s, de los dos que relaciona esa arista, es ese vértice $v$. 

- **Demostración:** 
  
  - (Si la arista cumple entonces hay un relax que lo cuenta) Sea $<u,v>$ una arista que participa en un camino de costo mínimo que parte de $s$ y sea $\delta(s,u) < \delta(s,v)$ entonces se sabe que por como funciona dijksrta $u$ va a salir primero del heap y en el momento que haga relax a sus adyacentes va a hacer relax a la arista $<u,v>$, y pueden ocurrir dos casos, que el relax de menor o que de igual. Si da menor entonces se asigna 1 por lo que se cuenta esta arista y si da igual se incrementa el valor por lo que también se cuenta esta arista. Tambien por propiedades del algoritmo de dijkstra se sabe que en el momento que se saca a $u$ del heap ya este tiene asignado su longitud de camino de costo mínimo y en el momento que se le haga relax a $<u,v>$ se le asigna el la longitud de camino de costo mínimo a $v$ o se mantiene (cuando da menor o da igual) y para ningun otro relax va a dar menor; por lo que una vez incrementado con una arista que cumple no se va a volver a asignar 1.
  
  - (Si el relax lo cuenta entonces es una arista que cumple) Sea $<u,v>$ una arista con la que se hizo relax y dió menor o igual.  En el caso de que la arista no pertenezca a un camino de costo mínimo entonces en ese relax no se le asignó la longitud del camino de costo mínimo a $v$ por lo que eventualmente va a venir el primer relax que le asigne el costo mínimo y se va a descontar todo lo que se contó anterior a eso y cualquier arista que de igual después de este momento (ya más nadie puede dar menor) es una arista que participa en un camino de costo mínimo por la **Propiedad 2**. Como se está haciendo el conteo en el array del vertice al que se le está haciendo relax y este por como funciona dijkstra tiene costo mayor o igual  a $u$ también queda demostrado que se almacena en el array del vertice más lejano a $s$ de los dos que relaciona la arista.

Luego por cada par de origen $s$ y destino $t$, calculamos las aristas que participan en un camino de $s$ a $t$ recorriendo los vértices y acumulando el valor de su array en la posición correspondiente a $s$ si cumple que $\delta(s,t) = \delta(s,u) + \delta(v,t)$, como el grafo es no dirigido  $\delta(v,t) = \delta(t,v)$ y se va a almacenar en un array bidimensional en la posición correspondiente  los pares de vértices $s$ y $t$ . Cuando se haga esto por cada par va a quedar en ese array en la posición correspondiente a cualqueir par de origen $s$ y destino $t$ la cantidad de aristas que participan en un camino de costo mínimo de $s$ a $t$.

- **Demostración:** Por la **Propiedad 3** sabemos que los vértices $u$ que cumplen $\delta(s,t) = \delta(s,u) + \delta(u,t)$ son vertices que participan en algún camino de costo mínimo; por lo que estamos acumulando son las aritstas que participan en algún camino de costo mínimo que parte de s donde el vértice más lejano a s, de los dos vértices que relaciona, pertenece a un camino de costo mínimo de s a t, que por la **Propiedad 1** son las aristas que participan en algún camino de costo mínimo de $s$ a $t$ . Cada arista es contada una única vez porque se cuenta solo en el vértice más lejano a $s$ 

### Análisis de la complejidad

Nuestro algoritmo consiste en realizar O($|V|$) veces un algoritmo de dijkstra con modificaciones que no afectan su complejidad por lo que en el peor caso es O($|V|^2$) Por lo que la complejidad de esa parte queda O($|V|^3$). El resto es un doble for por los posibles orígenes que es O($|V|^2$) y dentro un recorrido por el resto de los vértices que es O($|V|$) por lo que en total que O($|V|^3$); por lo que el algoritmo entero es O($|V|^3$)

Como se realiza dijkstra O($|V|$) veces, la complejidad de esa parte que da en O($|V|^3$) por lo que es tentador usar floyd warshall teniendo en cuenta que se conoce que en estos casos la complejidad es la misma pero su constante es menor; pero si se tiene en cuenta que la cantidad de puntos importantes debe ser considerablemente menor que el resto de los vértices y que en una ciudad los intercepciones de las calles tienen en promedio solo cuatro aristas, por lo que el grafo no debe ser denso, se puede decir que la orden de crecimiento de la solución que usa dijkstra es bastante menor que la que usa floyd warshall. En sí, esta primera parte que consiste en ejecutar el dijkstra modificado desde los $N$ puntos principales tiene como complejidad O($NElog(V)$) y la segunda parte tiene como complejidad O($N^2V$) por lo que la complejidad del algoritmo es O($N(Elog(V) + NV)$) cuando la solución con Floyd Warshall siempre es O($V^3$)

### El Tester

Para mostrar la correctitud del la solución se implementó un tester que genera un grafo aleatorio con la cantidad de vertices, aristas y puntos importantes especificados y compara  los resultados de nuestra con una solución más sencilla que se resuelve en O(E*V^2). Esta solución consiste en contar, por cada par posible de origenes y destino, las aristas $<u,v>$ que cumplen:

$$
min(\delta(origen,u),\delta(origen,u)) + w(<u,v>) + min(\delta(destino,v),\delta(destino,u)) = \delta(origen,destino)
$$

La propiedad que respalada esto es que una arista participa en un camino de costo mínimo de $s$ a $t$ ssi cumplen la propiedad anterior

- **Demostración**:
  
  - ($A \Rightarrow B$) supongamos que una arista pertenece a un camino de costo mínimo de $s$ a $t$. Si $w(<u,v>) \neq 0$ tiene que existir un vértice que es más cercano a $s$ que a $t$ y el otro tiene que ser más cercano a $t$ que a $s$, supongamos sin pérdida de generalidad que $u$ es más cercano a $s$ y que $v$ es más cercano a $t$. Siguiente a esto podemos notar que $\delta(s,t) = \delta(s,u) + w(u,v) + \delta(t,v)$ o lo que es equivalente $\delta(s,t) = min(\delta(s,u),\delta(s,v)) +w(u,v)+ min(\delta(t,u),\delta(t,v))$ 
  
  - ($B \Rightarrow A$) Sean $<u,v>$ una arista que cumple que  $w(u,v) \neq 0$  y $ \delta(s,t) = min(\delta(s,u),\delta(s,v)) + w(u,v) + min(\delta(t,u),\delta(t,v))$. Supongamos, sin pérdida de generalidad, que $min(\delta(s,u),\delta(s,v)) = \delta(s,u) $ , entonces no se puede cumplir $min(\delta(t,u),\delta(t,v)) = \delta(t,u)$ porque en tal caso podríamos construir un camino de costo mínimo que probara que $\delta(s,t) = \delta(s,u) + \delta(t,u)$, que es distinto que la longitud de camino mínimo que se plantea en la hipótesis. Por lo que sabemos que los mínimos tienen que escoger caminos que van a extremos distintos de la arista por lo que la ecuación de la hipótesis tiene la forma :$\delta(s,t) = \delta(s,u) + w(u,v) + \delta(t,v)$. Por lo que se puede construir un camino desde $s$ hasta el extremo más cercano a él de la arista (por ejemplo $u$), pasar por la arista y usar el camino de costo mínimo desde $t$ hasta $v$, por lo que esa arista partcipa en un camino de costo mínimo de $s$ a $t$.
