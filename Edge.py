## NAME       : VIDHUSHINI SRINIVASAN
## STUDENT ID : 801029539
''' 
************************************************************************************************************************************************************************
@File          Edge.py
 
@Title         Implementation of Edge Class

@Author        VIDHUSHINI SRINIVASAN

@Created       04/19/2018

************************************************************************************************************************************************************************
'''

import Constants

class Edge:
   """ 
        Edge class 
        
        attributes
        ===========
        verex_source   name of the source vertex 
        vertex_dest    name of the destination vertex             
        cur_stat       indicates if the vertex is up or down
        weight         holds the weight of the edge
                       from the given source to destination vertex
   """
   def __init__(self, source, dest,weight=0.0):
        self.verex_source = source
        self.vertex_dest=  dest
        self.cur_stat = Constants.UP
        self.weight = weight
        
   # set the current status of the edge as "UP"
   def edge_up(self):
       self.cur_stat = Constants.UP
       
   # set the current status of the edge as "DOWN"
   def edge_down(self):
       self.cur_stat = Constants.DOWN 
