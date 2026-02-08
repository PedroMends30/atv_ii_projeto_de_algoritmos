import heapq

def cookies(k, A):
    heapq.heapify(A)
    
    operations = 0
    
    while len(A) > 1 and A[0] < k:
        least_sweet = heapq.heappop(A)
        second_least_sweet = heapq.heappop(A)
        
        new_cookie = least_sweet + 2 * second_least_sweet
        
        heapq.heappush(A, new_cookie)
        
        operations += 1
    
    if A[0] >= k:
        return operations
    else:
        return -1
