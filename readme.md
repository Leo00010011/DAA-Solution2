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

**Propiedad 3**: Un vértice $v$ participa en un camino de costo mínimo  de $s$ a $t$ ssi $\delta(s,t) = \delta(s,v) + \delta(v,t)$ 

- **Demostración:** 
  
  - ($A \Rightarrow B$) Si un vertice participa en un camino de costo mínimo de $s$ a $t$ es evidente que se cumple que $\delta(s,t) = \delta(s,v) + \delta(v,t)$ 
  
  - Sea $v$ un vértice que cumple $\delta(s,t) = \delta(s,v) + \delta(v,t)$ entonces sea $P$ un camino de longitud mínima de $s$ a $v$ y $Q$ un camino de longitud mínima de $v$ a $t$ entonces la concatenación de estos dos caminos es un camino de $s$ a $t$ con longitud $\delta(s,t)$ por lo que es un camino de longitud mínima de $s$ a $t$ que contiene a $v$ 

Como mencionó en la sección pasada vamos a aprovechar la ejecución del algoritmo de dijkstra desde el origen $s$ para almacenar en una posición correspondiente a $s$ de un array que tiene cada vértice $v$ un valor que se va a ir incrementando con cada relax hacia ese vértice que de igual y asignandole 1 si da menor. Al terminar la ejecución en la posición correspondiente s en el array de  cada vértice $v$ va a estar la cantidad de aristas que participan en un camino de costo mínimo que parte desde $s$ que cumplen que su vertice más lejano s, de los dos que relaciona esa arista, es ese vértice $v$. 

- **Demostración:** 
  
  - (Si la arista cumple entonces hay un relax que lo cuenta) Sea $<u,v>$ una arista que participa en un camino de costo mínimo que parte de $s$ y sea $\delta(s,u) < \delta(s,v)$ entonces se sabe que por como funciona dijksrta $u$ va a salir primero del heap y en el momento que haga relax a sus adyacentes va a hacer relax a la arista $<u,v>$, y pueden ocurrir dos casos, que el relax de menor o que de igual. Si da menor entonces se asigna 1 por lo que se cuenta esta arista y si da igual se incrementa el valor por lo que también se cuenta esta arista. Tambien por propiedades del algoritmo de dijkstra se sabe que en el momento que se saca a $u$ del heap ya este tiene asignado su longitud de camino de costo mínimo y en el momento que se le haga relax a $<u,v>$ se le asigna el la longitud de camino de costomínimo a $v$ o se mantiene (cuando da menor o da igual) y para ningun otro relax va a dar menor; por lo que una vez incrementado con una arista que cumple no se va a volver a asignar 1.
  
  - (Si el relax lo cuenta entonces es una arista que cumple) Sea $<u,v>$ una arista con la que se hizo relax y dió menor o igual.  En el caso de que la arista no pertenezca a un camino de costo mínimo entonces en ese relax no se le asignó la longitud del camino de costo mínimo a $v$ por lo que eventualmente va a venir el primer relax que le asigne el costo mínimo y se va a descontar todo lo que se contó anterior a eso y cualquier arista que de igual después de este momento (ya más nadie puede dar menor) es una arista que participa en un camino de costo mínimo por la **Propiedad 2**. Como se está haciendo el conteo en el array del vertice al que se le está haciendo relax y este por como funciona dijkstra tiene costo mayor o igual  a $u$ también queda demostrado que se almacena en el array del vertice más lejano a $s$ de los dos que relaciona la arista.

Luego por cada par de origen $s$ y destino $t$, calculamos las aristas que participan en un camino de $s$ a $t$ recorriendo los vértices y acumulando el valor de su array en la posición correspondiente a $s$ si cumple que $\delta(s,t) = \delta(s,u) + \delta(v,t)$, como el grafo es no dirigido  $\delta(v,t) = \delta(t,v)$ y se va a almacenar en un array bidimensional en la posición correspondiente  los pares de vértices $s$ y $t$ . Cuando se haga esto por cada par va a quedar en ese array en la posición correspondiente a cualqueir par de origen $s$ y destino $t$ la cantidad de aristas que participan en un camino de costo mínimo de $s$ a $t$.

- **Demostración:** Por la **Propiedad 3** sabemos que los vértices que cumplen $\delta(s,t) = \delta(s,u) + \delta(v,t)$ son vertices que participan en algún camino de costo mínimo; por lo que estamos acumulando son las aritstas que participan en algún camino de costo mínimo que parte de s donde el vértice más lejano a s, de los dos vértices que relaciona, pertenece a un camino de costo mínimo de s a t, que por la **Propiedad 1** son las aristas que participan en algún camino de costo mínimo. Cada arista es contada una única vez porque se cuenta solo en el vértice más lejano a $s$ 

### Análisis de la complejidad
