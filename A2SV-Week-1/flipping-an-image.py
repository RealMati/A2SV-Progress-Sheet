class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i]=image[i][::-1]

            image[i]=[abs(1-bit) for bit in image[i]]

        return image