class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for x in nums1:
            
            cur = nums2.index(x)
            ind = cur + 1
            place = -1
            while ind < len(nums2):
                if nums2[ind] > nums2[cur]:
                    place = ind
                    break;
                ind += 1
            res.append(place if place == -1 else nums2[place])
            
        return res