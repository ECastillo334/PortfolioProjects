class MinBinaryHeap:
    #Creates a list that keeps track of the order of a min binary heap. The class can also get and delete the minimum.
    '''
        >>> h = MinBinaryHeap()
        >>> h.getMin
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
    '''

    def __init__(self):
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        # - YOUR CODE STARTS HERE -
        if self._heap == []:
            return None
        else:
            return self._heap[0]
        pass
    
    def _parent(self,index):
        # - YOUR CODE STARTS HERE -
        if self._heap == [] or index == 1:
            return None
        else:
            for k in range(len(self._heap)):
                if k == (index - 1):
                    if k/2 == k//2:
                        k -= 1
                    return self._heap[(k//2)]
        return None
        pass
        

    def _leftChild(self,index):
        # - YOUR CODE STARTS HERE -
        if self._heap == []:
            return None
        else:
            #index += 0
            if index*2 <= len(self._heap):
                return self._heap[(index*2)-1]
            else:
                return None
        pass


    def _rightChild(self,index):
        # - YOUR CODE STARTS HERE -
        if self._heap == []:
            return None
        else:
            #index += 0
            if (index*2)+1 <= len(self._heap):
                return self._heap[(index*2)]
            else:
                return None
        pass
 
      

    def insert(self,item):
        # - YOUR CODE STARTS HERE -
        if self._heap == []:
            self._heap.append(item)
        else:
            self._heap.append(item)
            
            currentI = len(self._heap) - 1
            #print(currentI)
            repeat = True
            """if currentI == 1:
                if self._heap[0] > item:
                    #print('I got this far')
                    self._heap[currentI-1], self._heap[-1] = self._heap[-1], self._heap[currentI-1]
            else:"""
            while repeat == True:
                #print(f"{self._parent(currentI)} and {self._heap[(currentI//2)-1]} and {currentI}")
                if self._parent(currentI + 1) != None and item < self._parent(currentI + 1):
                    if currentI/2 == currentI//2:
                        OorE = 1
                    else:
                        OorE = 0
                    #print(f"{self._parent(currentI + 1)} and {self._heap[(((currentI - OorE)//2))]} and {currentI}")
                    self._heap[currentI], self._heap[(((currentI - OorE)//2))] = self._heap[(((currentI - OorE)//2))], self._heap[currentI]
                    currentI = ((currentI - OorE)//2)
                    """if currentI == 0:
                            print('Not else')
                            repeat = False"""
                else:
                    #Debug:
                    #print(f"{self._parent(currentI-1)} and {currentI}")
                    #print('Else')
                    repeat = False
                    
        return None

        pass
            

    def deleteMin(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            value=self._heap[0]
            self._heap=[]
            return value 

        # - YOUR CODE STARTS HERE -
        else:
            value = self._heap.pop(-1)
            Rvalue = self._heap[0]
            currentI = 1
            self._heap[0] = value
            repeat = True
            while repeat == True:
                #Debug:
                #print(f"{self._heap} \n {self._leftChild(currentI)} \n {self._rightChild(currentI)} \n {currentI}")
                if self._leftChild(currentI) == None or self._rightChild(currentI) == None:
                    repeat = False
                elif self._leftChild(currentI) < self._rightChild(currentI) and self._leftChild(currentI) < self._heap[currentI - 1]:
                    self._heap[currentI - 1], self._heap[(currentI*2)-1] = self._heap[(currentI*2)-1], self._heap[currentI-1]
                    currentI = (currentI * 2)
                elif self._rightChild(currentI) <= self._rightChild(currentI) and self._rightChild(currentI) < self._heap[currentI - 1]:
                    self._heap[currentI - 1], self._heap[currentI*2] = self._heap[currentI*2],self._heap[currentI - 1]
                    currentI = (currentI * 2) + 1
                else:
                    repeat = False
                
            if self._leftChild(currentI) != None and self._leftChild(currentI) < self._heap[currentI - 1]:
                self._heap[currentI - 1], self._heap[(currentI*2)-1] = self._heap[(currentI*2)-1], self._heap[currentI-1]
            elif self._rightChild(currentI) != None and self._rightChild(currentI) < self._heap[currentI-1]:
                self._heap[currentI-1], self._heap[(currentI*2)] = self._heap[currentI*2], self._heap[currentI-1]
            return Rvalue
        pass



class PriorityQueue:
    #This class can create a heap out of a tuple to know the order and can return the min priority and delete the min priority.
    '''
        >>> priority_q = PriorityQueue()
        >>> priority_q.isEmpty()
        True
        >>> priority_q.peek()
        >>> priority_q.enqueue('sara',0)
        >>> priority_q
        [(0, 'sara')]
        >>> priority_q.enqueue('kyle',3)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle')]
        >>> priority_q.enqueue('harsh',1)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh')]
        >>> priority_q.enqueue('ajay',5)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay')]
        >>> priority_q.enqueue('daniel',4)
        >>> priority_q.isEmpty()
        False
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay'), (4, 'daniel')]
        >>> priority_q.enqueue('ryan',7)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay'), (4, 'daniel'), (7, 'ryan')]
        >>> priority_q.dequeue()
        (0, 'sara')
        >>> priority_q.peek()
        'harsh'
        >>> priority_q
        [(1, 'harsh'), (3, 'kyle'), (7, 'ryan'), (5, 'ajay'), (4, 'daniel')]
        >>> priority_q.dequeue()
        (1, 'harsh')
        >>> len(priority_q)
        4
        >>> priority_q.dequeue()
        (3, 'kyle')
        >>> priority_q.dequeue()
        (4, 'daniel')
        >>> priority_q.dequeue()
        (5, 'ajay')
        >>> priority_q.dequeue()
        (7, 'ryan')
        >>> priority_q.dequeue()
        >>> priority_q.isEmpty()
        True
    '''

    def __init__(self):
        self._items = MinBinaryHeap()
    
    def enqueue(self, value, priority):
        # - YOUR CODE STARTS HERE -
        self._items.insert((priority, value))
        pass
    
    def dequeue(self):
        # - YOUR CODE STARTS HERE -
        if self.isEmpty() == True:
            return None
        else:
            return self._items.deleteMin()
        pass
    
    def peek(self):
        # - YOUR CODE STARTS HERE -
        if self.isEmpty() == True:
            return None
        else:
            return self._items._heap[0][1]
        pass

    def isEmpty(self):
        # - YOUR CODE STARTS HERE -
        if self._items._heap == []:
            return True
        else:
            return False
        pass

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    __repr__ = __str__





class Graph:
    #Keeps track of a graph and uses dijkstras algorithm to find the shortest cost to get to a starting point.
    """
        >>> d_g1={
        ... 'A':[('B',2),('C',6),('D',7)],
        ... 'B':[('C',3),('G',12)],
        ... 'C':[('D',2),('E',3)],
        ... 'D':[('C',1),('E',2)],
        ... 'E':[('G',5)],
        ... 'F':[('D',2),('E',4)]}
        >>> my_graph = Graph(d_g1)
        >>> my_graph.addEdge('G', 'C', 4)
        >>> my_graph
        {'A': [('B', 2), ('C', 6), ('D', 7)], 'B': [('C', 3), ('G', 12)], 'C': [('D', 2), ('E', 3)], 'D': [('C', 1), ('E', 2)], 'E': [('G', 5)], 'F': [('D', 2), ('E', 4)], 'G': [('C', 4)]}
        >>> my_graph.dijkstra_table('A')   # ---> order of key,value pairs does not matter 
        {'A': 0, 'B': 2, 'C': 5, 'D': 7, 'E': 8, 'F': inf, 'G': 13}
    """
    def __init__(self, graph_repr=None):
        if graph_repr is None:
            self.vertList = {}
        else:
            self.vertList = graph_repr

    def __str__(self):
        return str(self.vertList)

    __repr__ = __str__

    def addVertex(self, key):
        if key not in self.vertList:
            self.vertList[key] = []
            return self.vertList

    def addEdge(self, frm, to, cost=1):
        if frm not in self.vertList:
            self.addVertex(frm)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[frm].append((to, cost))


    def dijkstra_table(self,start):
        # - YOUR CODE STARTS HERE -
        NewPQ = PriorityQueue()
        NewPQNoT = PriorityQueue()
        DT = {}
        visited = []
        for x in self.vertList: # x = dict key
            if x == start:
                DT[x] = 0
                for i in self.vertList[x]:
                    NewPQ.enqueue(i[0], i[1])   
            else:
                DT[x] = float("inf")
        while NewPQ.isEmpty() == False:
            thistuple = NewPQ.dequeue()
            DT[thistuple[1]] = thistuple[0]
            for i in self.vertList[thistuple[1]]:
                NewPQNoT.enqueue(i[0], i[1])
                x = i[0]
        visited.append(start)
        thistuple = NewPQNoT.dequeue()
        NewPQ.enqueue(thistuple[0], thistuple[1])
        while NewPQNoT.isEmpty() == False:
            NewPQNoT.dequeue()
        while NewPQ.isEmpty() == False:
            thistuple = NewPQ.dequeue()
            x = thistuple[0]
            for i in self.vertList[x]:
                NewPQ.enqueue(i[0], i[1])
            #smallest = (float("inf"), "NO")
            #print(NewPQ.peek())
            while NewPQ.isEmpty() == False:
                smallest = (float("inf"), "NO")
                thistuple = NewPQ.dequeue()
                if thistuple[0] + DT[x] < DT[thistuple[1]]:
                    DT[thistuple[1]] = thistuple[0] + DT[x]
                if thistuple[0] < smallest[0]:
                    smallest = thistuple
                if NewPQ.peek() == None and smallest[1] not in visited:
                    for i in self.vertList[smallest[1]]:
                        NewPQ.enqueue(i[0], i[1])
                    visited.append(smallest[1])
                    x = smallest[1]   

        for x in self.vertList:
            if x != start:
                for i in self.vertList[x]:
                    #print(i[0])
                    NewPQ.enqueue(i[0], i[1])
                while NewPQ.isEmpty() == False:
                    thistuple = NewPQ.dequeue()
                    if thistuple[0] + DT[x] < DT[thistuple[1]]:
                        DT[thistuple[1]] = thistuple[0] + DT[x]
                
        return DT
        """DT = {}
        for x in self.vertList: # x = dict key
            if x == start:
                DT[x] = 0
                for i in self.vertList[x]:
                    DT[i[0]] = i[1]
            else:
                if x not in DT:
                    DT[x] = float('inf')
                for i in self.vertList[x]: # i = tuples in x
                    if i[0] in DT:
                        #DT[i[0]] = i[1] + DT[x]
                        if i[1] + DT[x] < DT[i[0]]:
                            DT[i[0]] = i[1] + DT[x]
                    else:
                        DT[i[0]] = i[1] + DT[x]
        return DT"""
        pass
    

def run_tests():
    import doctest

    # Run start tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run start tests per class
    #doctest.run_docstring_examples(Graph, globals(), name='HW5',verbose=True)   

if __name__ == "__main__":
    run_tests()

