class Bit(object):
	def	 __init__(self, nums):
		self.size = len(nums)
		self.tree = [0 for _ in range(len(nums)+1)]
		for i in range(len(nums)):
			self.update(i, nums[i])

	def lowbit(self, i):
		return i & -i

	def update(self, i, delta):
		i += 1
		while i < self.size + 1:
			self.tree[i] += delta
			i += self.lowbit(i)

	def query(self, i):
		i += 1
		res = 0
		while i > 0:
			res += self.tree[i]
			i -= self.lowbit(i)
		return res

nums = [4,3,7,1,5]
b = Bit(nums)

print b.query(3) # should be the sum of 4,3,7,1