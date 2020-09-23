##### 剑指 Offer 39 
###### 数组中出现次数超过一半的数字


`数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。你可以假设数组是非空的，并且给定的数组总是存在多数元素。`

```
示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

限制：
1 <= 数组长度 <= 50000
```

###### 题解：
```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        ant = 0
        for num in nums:
            if res == num:
                ant = ant + 1
            elif res != num:
                if ant == 0:
                    res = num
                elif ant != 0:
                    ant = ant -1
        return res;
```