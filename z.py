def partition(nums, begin: int, end: int) -> int:
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

def nsort(nums, begin: int, end: int):
        if begin < end :
            index = partition(nums, begin, end)
            nsort(nums, begin, index - 1)
            nsort(nums, index + 1, end)



a = [3,30,34,5,9]
nsort(a,0,4)
print(a)