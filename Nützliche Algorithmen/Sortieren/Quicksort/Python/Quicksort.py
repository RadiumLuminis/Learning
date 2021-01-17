# Python program for implementation of Quicksort Sort 
  
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
  
  
def partition(arr, low, high): 
    i = (low-1)         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low, high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if arr[j] <= pivot: 
  
            # increment index of smaller element 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
  
  
def quickSort(arr, low, high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr, low, high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

def main():
    zahlen = [7, 9, 22, 30, 1, 40, 8, 5, 12, 15, 19, 20, 33, 2, 28, 21, 17, 18, 10, 29, 5, 1, 40, 1, 12, 35, 20, 16, 32, 40, 5, 24, 34, 35, 1, 15, 24, 37, 13, 39]
    n = len(zahlen)
    quickSort(zahlen, 0, n-1)
    print(zahlen)

if __name__ == "__main__":
    main()

