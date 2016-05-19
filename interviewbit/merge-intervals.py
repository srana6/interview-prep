"""
Merge Intervals


Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.



Fix one corner case:
	overlaps just one side in between

	A : [ (31935139, 38366404), (54099301, 76986474), (87248431, 94675146) ]
	B : (43262807, 68844111)

	(31935139, 38366404) (43262807, 76986474) (87248431, 94675146) 

"""



class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

	def __repr__(self):
		return "[%s, %s]" % (self.start, self.end)

class Solution:
	# @param intervals, a list of Intervals
	# @param new_interval, a Interval
	# @return a list of Interval
	def insert(self, intervals, new_interval):
		if new_interval.start > new_interval.end:
			new_interval.start, new_interval.end = new_interval.end, new_interval.start

		n = len(intervals)
		start = -1
		end = 0
		mid = [new_interval]

		while start + 1 < n and intervals[start + 1].start <= new_interval.start:
			start += 1
			end = start + 1

		while end < n and intervals[end].end < new_interval.end:
			end += 1

		
		if start == -1 and end == n:
			start = 0
		elif end == n:			
			start = n			
		elif start == -1:
			start = 0
			end = -1
		else:
			if max(intervals[start].start, new_interval.start) > min(intervals[start].end, new_interval.end):
				if max(intervals[end].start, new_interval.start) < min(intervals[end].end, new_interval.end):
					start += 1
					mid = [Interval(min(intervals[start].start, new_interval.start), max(intervals[end].end, new_interval.end))]
				else:					
					start += 1
					end -= 1

			else:
				mid = [Interval(min(intervals[start].start, new_interval.start), max(intervals[end].end, new_interval.end))]

		return (intervals[:start] + mid + intervals[end + 1:])


A = [Interval(31935139, 38366404), Interval(54099301, 76986474), Interval(87248431, 94675146)]
B = Interval(43262807, 68844111)
Solution().insert(A, B) 



