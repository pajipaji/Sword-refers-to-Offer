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

`办法2: 用快排， 快速排序：o(n*logn)  不稳定排序： `
`随机在数组中选1个数，小于等于这个数的数，统一放在左边，大于等于这个数的数统一放在右边，接下来在这个数的左右两个部分分别递归调用快排过程，这样整个数组就有序了。`
`快排划分过程：Partition过程：`
`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@将划分值放在数组最后一个位置（与最后一个位置元素互换）`
`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@设置1个小于等于区间，初始长度为0，放在整个数组左侧`
`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@从左向右遍历整个数组，若当前元素大于划分值，就继续遍历下一个元素，如果当前元素小于等于划分值，就将当前数与小于等于区间的下一个数交换，并令小于等于区间向右阔一个位置`
`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@在遍历完所有的元素直到最后一个元素时（倒数第二）将划分值与小于等于区间的下一个数交换，这就是一此完整的划分过程。o(N)`
```python3
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        self.nsort(nums, 0, len(nums)-1)
        res = ""
        for num in nums:
            res = res + str(num)
        return res

    def partition(self, nums: List[int], begin: int, end: int) -> int:
        pivot = nums[end]
        index = begin
        for i in range(begin, end):
            sant = str(nums[i]) + str(pivot)
            sans = str(pivot) + str(nums[i])
            if int(sant) < int(sans):
            # if nums[i] > pivot:
                nums[i], nums[index] = nums[index], nums[i]
                index = index + 1
        nums[index], nums[end] =  nums[end], nums[index]
        return index

    def nsort(self, nums: List[int], begin: int, end: int):
        if begin < end :
            index = self.partition(nums, begin, end)
            self.nsort(nums, begin, index - 1)
            self.nsort(nums, index + 1, end)

```



`办法3: 还是就是做个排序， 排序规则就是 3 和 30 比较的时候  把两个数字长度加到一样， 3 和 30比较 =》 33 和 30 比较， 例子35、354、356，35补5是对的，即补最后一位,  这个办法不对，提交代码用例卡在219条，一共222条用例，补第一位再加条件控制两数补位后相等的情况，最后一个用例没过。不纠结了，这个代码写的太长了，一定不是最优解`
```python3
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        stick = ['0000000000','1111111111','2222222222','3333333333','4444444444','5555555555','6666666666','7777777777','8888888888','9999999999']
        lnums = len(nums)
        for i in range(lnums):
            for j in range(i+1,lnums):
                s = ""
                si = 0
                sj = 0
                ant = len(str(nums[i]))
                ans = len(str(nums[j]))
                if ant < ans:
                    s = stick[int(str(nums[i])[0])][0:ans-ant]
                    si = int(str(nums[i]) + s)
                    sj = nums[j]
                    # print(s, si,sj)
                elif ant > ans:
                    s = stick[int(str(nums[j])[0])][0:ant-ans]
                    si = nums[i]
                    sj = int(str(nums[j]) + s)
                    
                else:
                    si = nums[i]
                    sj = nums[j]
                  
                if si > sj:
                    node = nums[i]
                    nums[i] = nums[j]
                    nums[j] = node
                elif si == sj:
                    node = max(nums[i],nums[j])
                    node2 = min(nums[i],nums[j])
                    nums[i] = node
                    nums[j] = node2
                <!-- print(nums[i],nums[j]) -->
         
        res = ""
        for num in nums:
            res = res + str(num)
        return res
```