class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = (len(nums1) + len(nums2))
        
        median_val = 2 if total_len %2 == 0 else 1
        median_ind = total_len // 2 - 1 if median_val == 2 else total_len // 2
        count = 0
        val = []
        x = 0
        y = 0
        cur = 0
        while len(val) != median_val:
            if x < len(nums1) and y < len(nums2):
                if nums1[x] < nums2[y]:
                    cur = nums1[x]
                    x += 1
                else:
                    cur = nums2[y]
                    y += 1
            elif x < len(nums1):
                cur = nums1[x]
                x += 1
            elif y < len(nums2):
                cur = nums2[y]
                y += 1
            if count == median_ind:
                val.append(cur)
                if median_val == 2:
                    median_ind += 1
        
            count += 1
        return sum(val) / len(val)