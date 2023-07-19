# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array indexlast_indexs
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0
	
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				if i == len(L)-1:
					None
				else:
					if L[i] > L[i+1] and list2.index(L[i])<list2.index(L[i+1]):
						global count
						count = count+1	
				arr[k] = L[i]
				i += 1
			else:
				if L[i] > R[j] and list2.index(L[i])<list2.index(R[j]) :
					
					count = count + 1
				if j == len(R)-1 :
					None
				else :
					if R[j] > R[j+1] and list2.index(R[j])<list2.index(R[j+1]) :
						count += 1
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any indexlast_index was left
		while i < len(L):
			if i == len(L)-1 :
				None
			else :
				if L[i] > L[i+1] and list2.index(L[i])<list2.index(L[i+1]) :
					count += 1
			arr[k] = L[i]
			i += 1
			k += 1

		
		
		while j < len(R):
			if j == len(R)-1 :
				None
			else :
				if R[j] > R[j+1] and list2.index(R[j])<list2.index(R[j+1]) :
					count += 1
			arr[k] = R[j]
			j += 1
			k += 1
	
	
	
list1 = []
n = int(input())
list1 = (input().split(" "))
list1 = [int(x) for x in list1]
count = 0
list2 = list1[:]



mergeSort(list1)
print(count)

