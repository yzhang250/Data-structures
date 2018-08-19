def quickSort(nums, low, high):
	if low >= high:
		return
	pivotal = nums[low]
	i = low + 1 #i stops at/points to num greater than pivotal
	j = high #j points to num less than pivotal
	while True:
		while i < high+1 and nums[i] < pivotal:
			i += 1
		while low < j and nums[j] > pivotal:
			j -= 1
		if i >= j:
			break
		nums[i], nums[j] = nums[j], nums[i]
		i += 1
		j -= 1
	nums[j], nums[low] = nums[low], nums[j]
	quickSort(nums,low,j-1)
	quickSort(nums, j+1, high)

def QuickSort(nums):
	return quickSort(nums, 0, len(nums)-1)

nums = [2,5,1,5,8,0,11,2,3,1,0,101,4,-2,19,15]
QuickSort(nums)
print nums