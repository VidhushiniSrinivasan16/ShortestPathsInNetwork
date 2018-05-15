## NAME       : VIDHUSHINI SRINIVASAN
## STUDENT ID : 801029539
''' 
************************************************************************************************************************************************************************
@File          MinBinaryHeap.py
 
@Title         Implementation of MinBinaryHeap Class

@Author        VIDHUSHINI SRINIVASAN

@Created       04/21/2018

************************************************************************************************************************************************************************
'''

class MinBinaryHeap:
    """ 
        MinBinaryHeap class 
        
        attributes
        ===========
        heap           heap array to hold elements
        size           current size of the heap
    """
    def __init__(self):
        self.heap = []
        self.size= 0

    # get the current heap size    
    def queue_size(self):
        return (self.size) 

    # add vertex to the heap and reorganize the elements
    # to satisfy min heap property
    def insert_vertex(self, vertex):
        index = self.size
        self.heap.append(None)
        while index > 0 and self.heap[int((index-1)/2)].dist > vertex.dist :
            self.heap[index] = self.heap[int((index-1)/2)]
            index = int((index-1) / 2)
        #print(index)
        self.heap[index]=vertex
        self.size+=1
        #print(len(self.heap))

    # get the minimum element from heap
    def extract_min(self):
        if self.size<=0:
            raise Exception("Heap Underflow")   
        min_element = self.heap[0]
        self.size-=1
        self.heap[0] = self.heap[self.size]
        del self.heap[self.size]
        self.min_heapify(0)
        return min_element

    # restore min heap property
    def min_heapify(self,index):
        left_index = 2 * index + 1
        right_index = left_index + 1
        smallest = index
        if left_index < self.size and self.heap[left_index].dist < self.heap[index].dist:
            smallest =  left_index
        if right_index < self.size and self.heap[right_index].dist < self.heap[smallest].dist:
            smallest = right_index
        if smallest != index:
            vertex = self.heap[index]
            self.heap[index] = self.heap[smallest]
            self.heap[smallest] = vertex
            self.min_heapify(smallest)
        
            

        
    
    
