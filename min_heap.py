#TC: getMin: O(1), bubbleUp: O(1), bubbleDown: O(1), insert: O(1), extractMin: O(1), size: O(1) 
#SC: O(n)


class Minheap: 
    def __init__(self): 
        self.heap = []  #initialize heap with an array

    def getMin(self): 
        return self.heap[0] #minimum element will always be in the top 

    def bubbleUp(self, index): 

        parentIndex = (index-1)//2 #assigning the parent index with the generalized formula to find the parent 

        if parentIndex<0: #if parent index is less than zero, it's just null 
            return        

        if self.heap[parentIndex] < self.heap[index]: #if parent index is less than current index, then just return as it's in the right order
            return 

        self.heap[parentIndex], self.heap[index] = self.heap[index],self.heap[parentIndex] #if null cases doesn't execute, swap the  current index with the parent index 
        self.bubbleUp(parentIndex) #call it recursively 

    def bubbleDown(self, index):  

        leftchild = 2*index+1 #formula to find the left child is to multiply the current index by 2 and add it by 1 
        rightchild = 2*index+2 #formula to find the left child is to multiply the current index by 2 and add it by 2 

        temp = index #assign the current index to a temporary variable 

        if leftchild < len(self.heap) and self.heap[temp] > self.heap[leftchild]:  #check whether left child is in the range and temp is greater than left child, if so, assign temp to left child 
            temp = leftchild 
        if rightchild < len(self.heap) and self.heap[temp] > self.heap[rightchild]:  #check whether right child is in the range and temp is greater than right child, if so, assign temp to right child 
            temp = rightchild 
        
        if temp == index: #finally, if temp is just the index, return by default
            return 

        
        self.heap[temp], self.heap[index] = self.heap[index], self.heap[temp] #if null cases doesn't execute, swap the  temp with the parent index 
        self.bubbleDown(temp) #call it recursively 


    def insert(self, key): 

        self.heap.append(key)  #just append the key to the heap
        self.bubbleUp(len(self.heap) - 1)  #now do the bubble up operation with last element as index 

    def extractMin (self): 

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0] #swap the first element with last element 
        temp = self.heap.pop()  #pop the top element and store it in temp
        self.bubbleDown(0) #now call bubbledown for index 0 again to get the next minimum element
        return temp  #just return the temp, as it's the minimum element

    def size(self): 
        return len(self.heap) #just return the length of the heap


