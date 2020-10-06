import Visualizer
import random
class Sort:
    def __init__(self,id):
        self.array = random.sample(range(50),50) #Random array of size X
        self.id = id # ID used to pick sorting algorithim

    def start_sort(self):
        if self.id == 1:
            self.bubble(self.array)
        elif self.id == 2:
            self.selection(self.array)
        elif self.id == 3:
            self.insertion(self.array)
        elif self.id == 4:
            self.mergesort(self.array, 0, len(self.array)-1)
        elif self.id == 5:
            self.quicksort(self.array,0,len(self.array)-1)
        return self.array

    # Bubble sort algo, with flag
    # "Works by repeatedly swapping the adjacent elements if they are in wrong order"
    # Time complexity average of N^2
    def bubble(self,array):
        # Flag checks if any swaps happened, if not array is already sorted
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    Visualizer.update_screen(array, "Bubble Sort", j, j+1)
                    array[j], array[j + 1] = array[j + 1], array[j]


    # Selection sort algo
    # "Works by repeatedly finding the minimum element from unsorted part and putting it at the beginning of already sorted array"
    # Time complexity average of N^2
    def selection(self,array):
        for i in range(len(array)):
            # minimum value at position i
            minimum = i;
            for j in range(i+1, len(array)):
                if array[j] < array[minimum]:
                    minimum = j
            Visualizer.update_screen(array, "Selection sort", i, minimum)
            array[i], array[minimum] = array[minimum], array[i]


    # Insertion sort algo
    # "array is virtually split into a sorted and an unsorted part.
    # Values from the unsorted part are picked and placed at the correct position in the sorted part."
    # Time complexity average of N^2
    def insertion(self,array):
        for i in range(1, len(array)):
            curr = array[i]
            # Move elements of already sorted portion one element up if greater then curr value
            sPart = i-1
            while sPart >= 0 and curr < array[sPart]:
                array[sPart+1] = array[sPart]
                sPart = sPart-1
            Visualizer.update_screen(array, "Insertion sort", sPart, i)
            array[sPart+1] = curr


    # Merge sort algo
    # "Merge Sort is a Divide and Conquer algorithm.
    # It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves."
    # Time complexity average of N*log(N)
    def mergesort(self,array, l, r):
        # Keep dividing array in half until each array is length 1,
        if l >= r:
            return
        m = (l+r)//2
        self.mergesort(array, l, m)
        self.mergesort(array, m+1, r)
        self.merge(array, l, r, m)


    # Used to do the actual merging of two arrays
    def merge(self, array, left_index, right_index, middle):
        # Second param is non-inclusive thus we add 1
        left_copy = array[left_index : middle + 1]
        right_copy = array[middle + 1 : right_index + 1]
        # Values to keep track of where we are in each 'sub-array'
        left_copy_index = 0
        right_copy_index = 0
        sorted_index = left_index #this is where previous problem was, set to left_index of total array passed in, not left_copy_index as that is different value
        # Fill up new array with portions of each sub array
        # until we run out of elements in one array
        while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
            if left_copy[left_copy_index] <= right_copy[right_copy_index]:
                Visualizer.update_screen(array, "Merge sort", sorted_index, left_copy_index)
                array[sorted_index] = left_copy[left_copy_index]
                left_copy_index = left_copy_index + 1
            else:
                Visualizer.update_screen(array, "Merge sort", sorted_index, right_copy_index)
                array[sorted_index] = right_copy[right_copy_index]
                right_copy_index = right_copy_index + 1
            sorted_index = sorted_index+1
        # Either ran out of elements in left or right array
        # Need to while loops to fill in whichever array has remaining elements
        while left_copy_index < len(left_copy):
            Visualizer.update_screen(array, "Merge sort", sorted_index, left_copy_index)
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
            sorted_index = sorted_index + 1
        while right_copy_index < len(right_copy):
           Visualizer.update_screen(array, "Merge sort", sorted_index, right_copy_index)
           array[sorted_index] = right_copy[right_copy_index]
           right_copy_index = right_copy_index + 1
           sorted_index = sorted_index + 1

    # Quick sort algo
    # "QuickSort is a Divide and Conquer algorithm.
    # It picks an element as pivot and partitions the given array around the picked pivot"
    # Time complexity average of N*log(N)
    def quicksort(self, array, low, high):
        if low < high:
            # pindex is partition index, arr[pindex] is now in the relative middle
            pindex = self.partition(array, low, high)

            self.quicksort(array, low, pindex-1)
            self.quicksort(array, pindex, high)
    # Places all smaller elements to left of pivot
    # and all larger elements to right of pivot
    def partition(self, array, low, high):
        # This is the index of the smaller element
        i = (low-1)
        # Pivot is last element
        pivot = array[high]
        for j in range(low, high):
            # if array element is smaller then pivot
            # then shift low index up
            if array[j] < pivot:
                i += 1
                Visualizer.update_screen(array, "Quick Sort", i, j)
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        return i+1







