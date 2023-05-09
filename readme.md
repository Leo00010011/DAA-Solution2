# Segundo problema de DAA

### Integrantes:

* Leonardo Ulloa Ferrer

* Roxana Peña Mendieta

### Descripcion del problema

### La idea de la solución

La solución se basa en la propiedad de que el conjunto de las aristas que participan en un camino de costo mínimo de $s$ a $t$, es igual a la intercepción del conjunto de las aritstas que participan en algún camino de costo mínimo que parte de $s$, con el conjunto de las aristas donde el vértice más lejano a $s$, de los dos vértices que relaciona, pertenece a un camino de costo mínimo de $s$ a $t$. 

Luego para calcular las aristas que participan en algun camino de costo mínimo que parte de $s$ usamos la propiedad de que una arista $<u,v>$ con $\delta(s,u) < \delta(s,v)$ cumple esto ssi $\delta(s,u) = \delta(s,u) + w(<u,v>)$

Para calcular los vértices que participan en un camino de costo mínimo de $s$ a $t$ usamos la propiedad de que un vértice cumple esto ssi $\delta(s,t) = \delta(s,v) + \delta(v,t)$

Luego se puede utilizar el algoritmo de dijkstra para calcular, para cada posible origen, los caminos de costo mínimo y la aristas que participen en algunos de estos caminos. Para esto vamos a asignarle un array de tamaño $|V|$ a cada vértice $v$, donde almacenaremos en el índice $i$ la cantidad de aristas que cumplen que: 

- participan en un camino de costo mínimo que parte de $V_i$ 

- de los dos vértices que relaciona la arista el más lejano a ese origen es $v$

Los valores de este array los calcularemos aprovechando el relax que necesita hacer dijkstra, haciendo incrimentar el valor de la posición $i$ si da igual y asignandole 1 si da menor.

Teniendo calculado esto se puede resolver en O($|V|$) las aristas que participan en un camino de costo mínimo de $s$ a $t$ acumulando lo que tiene cada vertice que participa en un camino de costo mínimo de $s$ a $t$ en su array en la posición correspondiente a $s$. Por lo que iterando por cada posible origen y final y haciendo lo anterior se puede resolver esto en O($|V|^3$) y hacer $|V|$ dijkstras es O($|V|^3$) también por lo que la solución quedaría O($|V|^3$)

### El algoritmo

### Demostración de la Correctitud

**Propiedad 1** :el conjunto de las aristas que participan en un camino de costo mínimo de $s$ a $t$, es igual a la intercepción del conjunto de las aritstas que participan en algún camino de costo mínimo que parte de $s$, con el conjunto de las aristas donde el vértice más lejano a $s$, de los dos vértices que relaciona, pertenece a un camino de costo mínimo de $s$ a $t$.

- **Demostración**: 
  
  * ($A \sub B$) Si una arista pertenece a un camino de costo mínimo de $s$ a $t$ entonces es lógico que esta arista pertenezca a algún camino de  costo mínimo que parte de $s$ y que ambos de los vértices que relacione pertenezcan a un camino de costo mínimo de $s$ a $t$
  
  * ($B \sub A$) Luego sea $<u,v>$ una arista que pertenece a algún camino de costo mínimo de $s$, supongamos $\delta(s,u) < \delta(s,v)$  y que $v$ pertenece a algún camino de costo mínimo de $s$ a $t$. Luego sea $P$ el camino de costo mínimo de $s$ a $t$ que contiene a $v$ y sea $Q$ el camino de costo mínimo que parte de $s$ que contiene la arista $<u,v>$. Luego el subcamino de $Q$ hasta $v$ contiene la arista $<u,v>$ porque $v$ está más alejado de $s$ que $u$ y la longitud de este subcamino es igual a la longitud del subcamino hasta $v$ en $P$; por lo que al sustituir en $P$ su subcamino hasta $v$, por el subcamino hasta $v$ de $Q$ se obtiene un camino de $s$ a $t$ con la misma longitud de $P$ que contiene a $<u,v>$ por lo que pertenece a un camino de longitud mínima de $s$ a $t$ 

**Propiedad 2**: una arista $<u,v>$ con $\delta(s,u) < \delta(s,v)$ pertenece a algún camino de costo mínimo que parte de $s$ ssi $\delta(s,v) = \delta(s,u) + w(<u,v>)$ 

- **Demostración**:
  
  - ($A \Rightarrow B$) Si una arista $<u,v>$ con $\delta(s,u) < \delta(s,v)$ participa en algún camino de costo mínimo que parte de $s$, entonces sea $P$ uno de estos caminos ; su subcamino de $s$ a $v$ tiene longitud $\delta(s,v)$ y como termina con los vértices $u$ y $v$, la longitud de este camino también es igual a $\delta(s,u) + w(<u,v>)$. Por lo que $\delta(s,v) = \delta(s,u) + w(<u,v>)$ 
  
  - ($B \Rightarrow A$) Si $\delta(s,v) = \delta(s,u) + w(<u,v>)$ entonces sea $P$ un camino de longitud mínima de $s$ a $u$ y añadele al final a $v$ a travez de la arista $<u,v>$ y se tiene un camino de $s$ a $v$ con longitud $\delta(s,v)$ por lo que este camino es un camino de longitud mínima de $s$ a $v$ en el que  $<u,v>$ participa



### Análisis de la complejidad
