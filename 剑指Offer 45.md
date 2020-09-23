##### 剑指 Offer 45 
###### 把数组排成最小的数

`输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。`

```
示例 1:
输入: [10,2]
输出: "102"

示例 2:
输入: [3,30,34,5,9]
输出: "3033459"

提示:
0 < nums.length <= 100

说明:
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
```

###### 题解：
`办法1: 用选择排序法，（一开始在0 - N-1 上选出一个最小值，把它放在0上（与0号位置的元素交换），然后在1 - N-1上选出最小值放在1上（与1上元素交换）直到从0 - N-1到 N-1 - N-1 时整个数组就变得有序了。）`
```python3
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        sant: str
        sans: str
        lnums = len(nums)
        for i in range(lnums):
            for j in range(i+1,lnums):
                sant = str(nums[i]) + str(nums[j])
                sans = str(nums[j]) + str(nums[i])
                if int(sant) > int(sans):
                    node = nums[i]
                    nums[i] = nums[j]
                    nums[j] = node
        res = ""
        for num in nums:
            res = res + str(num)
        return res
```

`办法2: 还是就是做个排序， 排序规则就是 3 和 30 比较的时候  把两个数字长度加到一样， 3 和 30比较 =》 33 和 30 比较， 例子35、354、356，35补5是对的，即补最后一位`
