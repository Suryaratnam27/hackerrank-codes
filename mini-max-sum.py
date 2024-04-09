def mms(nums):
    block1=nums[0:4]
    block2=nums[-4: ]

    min=sum(block1)
    max=sum(block2)

    return min,max 

a,b=mms([1,2,3,4,5,6])
print(a,b)


