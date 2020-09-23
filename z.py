def minNumber(nums):
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
                    s = stick[int(str(nums[i])[ant-1])][0:ans-ant]
                    si = int(str(nums[i]) + s)
                    sj = nums[j]
                    print(s, si,sj)
                elif ant > ans:
                    s = stick[int(str(nums[j])[ans-1])][0:ant-ans]
                    si = nums[i]
                    sj = int(str(nums[j]) + s)
                    
                else:
                    si = nums[i]
                    sj = nums[j]
                  
                if si > sj:
                    node = nums[i]
                    nums[i] = nums[j]
                    nums[j] = node
                
        res = ""
        for num in nums:
            res = res + str(num)
        return res            

b = [824,938,1399,5607,6973,5703,9609,4398,8247]
a = minNumber(b)
print(a)



c ="1399439856075703697382478249389609"
print(a == c)