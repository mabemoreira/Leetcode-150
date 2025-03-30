class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if(n == 0):
            del nums1[m:]
        elif(m == 0):
            for i in range(n):
                nums1[i] = nums2[i]
            del nums1[n:]
        i = 0
        j = 0
        k = 0
        copy = nums1[0:m]
        while j < n and i < m:
            if(copy[i] <= nums2[j]):
                nums1[k] = copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k+=1

        while j < n:
            nums1[k] = nums2[j]
            k+=1 
            j += 1
        
        while i < m:
            nums1[k] = copy[i]
            k+=1
            i +=1