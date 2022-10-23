class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ret_image = [[0 if x==1 else 1 for x in im][::-1] for im in image]
        return ret_image