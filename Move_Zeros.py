class solutions(object):
    def move_zeros(self,nums):
        non_zero=0 #acts as a pointer
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[non_zero]=nums[i]
                non_zero+=1 #the pointer moves to next index  
        for i in range(non_zero,len(nums)):
                nums[i]=0
nums=[0,1,0,2,3,4]
object=solutions().move_zeros(nums)
print(nums)