class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numberDict = collections.defaultdict(int)
        for number in nums:
            numberDict[number] += 1
        heap = []
        record = 0
        for key in numberDict.keys():
            if record < k:
                heap.append((key, numberDict[key]))
                record += 1
            else:
                break
        heap = self.buildHeap(heap, k)
        i = 0
        for key in numberDict.keys():
            i += 1
            if i <= k:
                continue
            if numberDict[key] < heap[0][1]:
                continue
            else:
                heap[0] = (key, numberDict[key])
                heap = self.modifyHeap(heap, 0, k)
        return [_[0] for _ in heap]

    def buildHeap(self, heap, k):
        for i in range(len(heap) // 2 - 1, -1, -1):
            self.modifyHeap(heap, i, k)
        return heap
        
    def modifyHeap(self, heap, i, k):
        largest = i
        l = self.left(i)
        if l < k and heap[i][1] > heap[l][1]:
            largest = l
        r = self.right(i)
        if r < k and heap[largest][1] > heap[r][1]:
            largest = r
        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            self.modifyHeap(heap, largest, k)
            return heap
        return heap

    def left(self, i):
        return (2 * i) + 1
    
    def right(self, i):
        return (2 * i) + 2

    def parent(self, i):
        return ((i + 1) // 2) - 1
