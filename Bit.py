class Bit(object):
	def	 __init__(self, nums):
		self.nums = nums
		self.tree = [0 for _ in range(len(nums))]

	def lowbit(self, i):
		return i & -i

	def update(self, i, delta):
		while i <:
