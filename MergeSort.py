def mergeSort(nums, low, high):
	if high == low:
		return
	mid = low + (high-low)/2
	mergeSort(nums, low, mid)
	mergeSort(nums, mid+1, high)
	i = low
	j = mid + 1
	tmp = []
	while i <= mid and j <= high:
		if nums[i] > nums[j]:
			tmp.append(nums[j])
			j += 1
		else:
			tmp.append(nums[i])
			i += 1
	while i <= mid:
		tmp.append(nums[i])
		i += 1
	while j <= high:
		tmp.append(nums[j])
		j += 1
	for i in range(low, high+1):
		nums[i] = tmp[i-low]

def MergeSort(nums):
	if not nums:
		return
	mergeSort(nums, 0, len(nums)-1)

nums = [2,5,1,5,8,0,11,2,3,1,0,101]
MergeSort(nums)
print nums
