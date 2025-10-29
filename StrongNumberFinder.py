import math

class StrongNumberFinder:
    def __init__(self, start, end):
        """Initialize with range values"""
        self.start = start
        self.end = end

    def is_strong(self, num):
        """Check if a number is Strong"""
        digits = [int(d) for d in str(num)]
        total = sum(math.factorial(d) for d in digits)
        return total == num

    def find_strong_numbers(self):
        """Return all Strong numbers in the given range"""
        strong_nums = []
        for n in range(self.start, self.end + 1):
            if self.is_strong(n):
                strong_nums.append(n)
        return strong_nums

    def show_result(self):
        """Display all Strong numbers"""
        result = self.find_strong_numbers()
        if result:
            print(f"✅ Strong Numbers between {self.start} and {self.end} are: {result}")
        else:
            print(f"❌ No Strong Numbers found between {self.start} and {self.end}.")



