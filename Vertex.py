## NAME       : VIDHUSHINI SRINIVASAN
## STUDENT ID : 801029539
''' 
************************************************************************************************************************************************************************
@File          Vertex.py
 
@Title         Implementation of Vertex Class

@Author        VIDHUSHINI SRINIVASAN

@Created       04/19/2018

************************************************************************************************************************************************************************
'''


import Constants

class Vertex:
   """ 
        Vertex class 
        
        attributes
        ===========
        name           name of the vertex 
        adj_lis        contains list of adjacent vertices
        dist           stores current shortest distance to the vertex from a source vertex
        prev           holds the predecessor of the vertex               
        cur_stat       indicates if the vertex is up or down
   """
   def __init__(self, name):
      self.name = name
      self.adj_lis=[]
      self.dist = None
      self.prev = None
      self.cur_stat = Constants.UP

   # set the current status of the vertex as "UP"
   def vertex_up(self):
       self.cur_stat = Constants.UP

   # set the current status of the vertex as "DOWN"
   def vertex_down(self):
       self.cur_stat = Constants.DOWN 

   # reset all the vetex distances to infinity and
   # initialize predecessors to None 
   def reset(self):
       self.dist = Constants.INFINITE
       self.prev = None

    
