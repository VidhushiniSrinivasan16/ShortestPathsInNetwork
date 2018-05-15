                                                                          @@@@@ Shortest Paths in a Network @@@@@

NAME       : VIDHUSHINI SRINIVASAN
STUDENT ID : 801029539

PROGRAM AND DATA STRUCTURE DESIGN
============================================================================================================================
The program contains five different classes Graph, Edge, Vertex, Constants and MinBinaryHeap

Graph class
------------------------------------------------------------------------------------------------ 
        
        
        attributes
        ===========
        vertex_map           holds all the vertex names as keys and
                             vertex object as values
        edge_map             holds all the start vertex names as keys
                             whose value has a dictionary with end vertex names as
                             as keys and edge object as values
------------------------------------------------------------------------------------------------
In addition to these attributes , we have other methods like add_edge, delete_edge(), print_graph(), reachable() etc to dynamically 
update networks and to get the current configuration of the network.

Edge class
------------------------------------------------------------------------------------------------
        
        
        attributes
        ===========
        verex_source   name of the source vertex 
        vertex_dest    name of the destination vertex             
        cur_stat       indicates if the vertex is up or down
        weight         holds the weight of the edge
                       from the given source to destination vertex
--------------------------------------------------------------------------------------------------
It also has methods like edge_down() and edge_up() to dynamically update networks.

Vertex class

--------------------------------------------------------------------------------------------------- 
        
        
        attributes
        ===========
        name           name of the vertex 
        adj_lis        contains list of adjacent vertices
        dist           stores current shortest distance to the vertex from a source vertex
        prev           holds the predecessor of the vertex               
        cur_stat       indicates if the vertex is up or down
----------------------------------------------------------------------------------------------------
It also has methods like vetex_down(), vertex_up() and reset() to dynamically update networks.

MinBinaryHeap class
---------------------------------------------------------------------------------------------------- 
        MinBinaryHeap class 
        
        attributes
        ===========
        heap           heap array to hold elements
        size           current size of the heap
-----------------------------------------------------------------------------------------------------
It also has methods like add_vertex(), extract_min(), min_heapify() etc to support binary heap operations.

Datastructures used
___________________

* python dictionary to efficiently implement vertex and edge mappings.
* use of python's list for adjacency list representation to store outgoing edge from every vertex
* classes to enable easy representation and use of objects and support for object oriented programming

Files
=================================================================================================================================
* Graph.py               main source code containing the entire logic for dynamic upgradation of network
* Edge.py                file containg edge class and its appropriate methods
* Vertex.py              file containing vertex class and its appropriate methods
* MinBinaryHeap.py       file containing min heap implementation and its methods
* Constants.py           file containing necessary constants to be used across other classes
* Project2.pdf           The file with instructions for this project
* README.txt             The file that contains information about program and data structure design
                         and instructions on how to execute the source code.
*network.txt             The file containing the network details
*queries.txt             The file containing queries for dynamic network updates
*output.txt              The file containg output for the given queries

Merits/Demerits of the program
=================================================================================================================================
*This program can work for any type of dynamic updates on network and helps in finding the shortest path for the current 
network state. 

Programming Language/ Pre Requisites
=================================================================================================================================
Programming Language:   Python

Pre Requisites:	        Python   - Version: 3.6.2 64 bit
			IDE used - Python's Integrated Development and Learning Environment(IDLE) - Version - 3.6.2
Usage Instructions
=================================================================================================================================
* Place the source code (.py files) and the input files in the same folder and open the command prompt(CMD)from that folder.
* The Graph.py file can be run from the command prompt from the folder where the files are placed using 
  the command: python Graph.py network.txt<queries.txt>output.txt
* The arguments network.txt, queries.txt  and the output file can be changed accordingly.


