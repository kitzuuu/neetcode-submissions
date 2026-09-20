class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_chart = Counter(nums)
        output=[]
        for num, freq in frequency_chart.most_common(k):
            output.append(num)
        return output