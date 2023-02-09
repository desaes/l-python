import random

class Array:
    @staticmethod
    def reverse(array):
        try:
            size = len(array)
            for i in range(0, size//2):
                """
                save = array[i]
                array[i] = 
                array[size - i - 1] = save
                """
                array[i], array[size - i - 1] = array[size - i - 1], array[i]
        except Exception as e:
            print(e)
        return array

    @staticmethod
    def reverse2(array):
        try:
            # start index
            start = 0
            # end index
            end = len(array) - 1
            while start < end:
                """
                save = array[start]
                array[start] = array[end]
                array[end] = save
                """
                array[start], array[end] = array[end], array[start]
                start = start + 1
                end = end - 1
        except Exception as e:
            print(e)
        return array
    
    @staticmethod
    def is_palindrome(array):
        try:
            # start index
            start = 0
            # end index
            end = len(array) - 1
            while start < end:
                if array[start] != array[end]:
                    return False
                start = start + 1
                end = end - 1
            return True
        except Exception as e:
            print(e)

    # just do a reverse and compare or maybe, change the reverse function to work with strings and use it
    @staticmethod
    def is_palindrome2(array):
        if array == array[::-1]:
            return True
        return False
    
    # same or modify the reverse function
    @staticmethod
    def reverse_int(i):
        return int(str(i)[::-1])
    
    @staticmethod
    def reverse_int2(i):
        reversed_integer = 0
        remainder = 0
        while i > 0:
            remainder = i % 10
            reversed_integer = reversed_integer * 10 + remainder
            i = i // 10
        return reversed_integer
    
    @staticmethod
    def is_anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        if sorted(str1) == sorted(str2):
            return True
        return False
    
    @staticmethod
    def swap(nums, i1, i2):
        nums[i1], nums[i2] = nums[i2], nums[i1]
    
    # review!
    # https://www.udemy.com/course/algorithms-and-data-structures-in-python/learn/lecture/30236278
    @staticmethod
    def dutch_flag_problem(nums, pivot=1):
        i, j = 0, 0
        k = len(nums) - 1
        while j <= k:
            if nums[j] < pivot:
                Array.swap(nums, i, j)
                i=i+1
                j=j+1
            elif nums[j] > pivot:
                Array.swap(nums, k, j)
                k=k-1
            else:
                j=j+1
        return nums

    @staticmethod
    def watter_trap(nums):
        if len(nums) < 3:
            return 0
        max_right = []
        max_left = []
        result = []
        j = 0
        max_left.append(0)
        for i in range(1, len(nums)):
            if nums[i - 1] > j:
                j = nums[i - 1]
            max_left.append(j)
        
        k = 0
        max_right.append(0)
        for i in range(len(nums), 1, -1):
            if nums[i - 1] > k:
                k = nums[i - 1]
            max_right.insert(0, k)
        
        for i in range(1, len(nums)):
            r = min(max_left[i] , max_right[i]) - nums[i]
            if r < 1:
                result.append(0)
            else:
                result.append(r)
        return sum(result)

    @staticmethod
    def watter_trap2(nums):
        if len(nums) < 3:
            return 0

        left_max = [0 for _ in range(len(nums))]
        right_max = [0 for _ in range(len(nums))]

        # dealing with the left max values
        for i in range(1, len(nums)):
            left_max[i] = max(left_max[i - 1], nums[i - 1])

        # dealing with the right max values
        for i in range(len(nums) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i + 1])

        # consider all the items in O(N) and sum up the trapped rain water units
        trapped = 0

        for i in range(1, len(nums) - 1):
            if min(left_max[i], right_max[i]) > nums[i]:
                trapped += min(left_max[i], right_max[i]) - nums[i]

        return trapped

        
if __name__ == "__main__":
    #a = [1,2,3,4,5]
    #t = 'aaaaaabvbaaaaaa'
    #print(Array.reverse_int2(12340))
    #print(Array.is_anagram('abc', 'cda'))
    #print(Array.dutch_flag_problem([2,0,1,1,2,0,0,1]))
    print(Array.watter_trap([2,1,0,3,0,2,0,1,0,4]))
    print(Array.watter_trap2([2,1,0,3,0,2,0,1,0,4]))

    print(Array.watter_trap([1, 0, 2, 1, 3, 1, 2, 0, 3]))
    print(Array.watter_trap2([1, 0, 2, 1, 3, 1, 2, 0, 3]))