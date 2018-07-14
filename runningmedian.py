'''
변화하는 중간값
https://algospot.com/judge/problem/read/RUNNINGMEDIAN
@ Jae Kyun Kim
'''
class MaxHeap():
    def __init__(self):
        self.size = 0
        self.arr = list()
        self.arr.append('') ## To make index start from 1
    
    def heapify(self, i):
        largest = i
        left = 2 * i     
        right = 2 * i + 1    
        
        if left < self.size and self.arr[largest] < self.arr[left]:
            largest = left
    
        if right < self.size and self.arr[largest] < self.arr[right]:
            largest = right
    
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]  
            self.heapify(largest)

    def push(self, data):       
        self.size += 1

        ## 힙의 개수가 2 이상일 때, 
        if self.size > 1:
            self.arr.append(data)
            child = self.size
            parent = int(self.size/2)
            
            while parent >= 1:
                if self.arr[child] > self.arr[parent]:
                    ## Swap
                    self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
                    parent = int(parent/2)
                    child = int(child/2)
                else:
                    break

        ## 처음 데이터가 힙으로 들어올 때,
        else:
            self.arr.append(data)

    def pop(self):
        ## Swap with last node
        self.arr[1], self.arr[self.size] = self.arr[self.size], self.arr[1]
        self.size -= 1
        ## heapify
        self.heapify(1)

    def top(self):
        if self.size != 0:
            return self.arr[1]
    
    def print(self):
        for i in range(1, self.size+1):
            print(self.arr[i], )
        print('\n')

class MinHeap():
    def __init__(self):
        self.size = 0
        self.arr = list()
        self.arr.append('') ## To make index start from 1
    
    def heapify(self, i):
        smallest = i
        left = 2 * i     
        right = 2 * i + 1    
        
        if left < self.size and self.arr[smallest] > self.arr[left]:
            smallest = left
    
        if right < self.size and self.arr[smallest] > self.arr[right]:
            smallest = right
    
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]  
            self.heapify(smallest)

    def push(self, data):       
        self.size += 1

        ## 힙의 개수가 2 이상일 때, 
        if self.size > 1:
            self.arr.append(data)
            child = self.size
            parent = int(self.size/2)
            
            while parent >= 1:
                if self.arr[child] < self.arr[parent]:
                    ## Swap
                    self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
                    parent = int(parent/2)
                    child = int(child/2)
                else:
                    break

        ## 처음 데이터가 힙으로 들어올 때,
        else:
            self.arr.append(data)

    def pop(self):
        ## Swap with last node
        self.arr[1], self.arr[self.size] = self.arr[self.size], self.arr[1]
        self.size -= 1
        ## heapify
        self.heapify(1)

    def top(self):
        if self.size != 0:
            return self.arr[1]
    
    def print(self):
        for i in range(1, self.size+1):
            print(self.arr[i], )
        print('\n')

if __name__ == '__main__':
    # test_case = int(input())

    # for i in range(test_case):
    #     command = input()
    #     argument = command.split(' ')
    #     n, a, b = int(argument[0]), int(argument[1]), int(argument[2])

    #     previous_value = 1983
    #     max_heap = MaxHeap(previous_value)
    #     min_heap = MinHeap()

    #     '''
    #     1. max heap의 크기는 min heap의 크기와 같거나 1 더 크다.
    #     2. max heap의 root 값은 min heap의 root 값보다 작거나 같다.
    #     '''        
    #     for i in range(0, n):
    #         next_value = (previous_value * a + b) & 20090711

    #         ## 힙의 개수가 같으면 max heap에 넣는다
    #         if max_heap.size == min_heap.size:
    #             max_heap.push(next_value)
    #         ## 힙의 개수가 다르면 min heap에 넣는다
    #         else:
    #             min_heap.push(next_value)

    #         ## 힙이 둘다 비어있지 않고, max heap의 최대 값이 min heap의 최소 값보다 크다면 root 값끼리 바꾼다
    #         if min_heap.size != 0 and max_heap.size != 0 and min_heap.top() < max_heap.top():
    #             a = max_heap.top()
    #             b = min_heap.top()
    #             max_heap.pop()
    #             min_heap.pop()
    #             max_heap.push(b)
    #             min_heap.push(a)
            
    #         result = (result + max_heap.top()) & 20090711
        
    #     print(result)

    heap = MaxHeap()
    heap.push(3)    
    heap.push(7)    
    heap.push(6)    
    heap.push(5)    
    heap.push(9)    
    heap.push(1)
    heap.print()    

        


