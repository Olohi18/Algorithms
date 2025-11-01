# def median_of_medians(list_l: list[int]):
#     target_index:int = len(list_l)//2
#     # indices_dict = list[i], i for i in range(len(list_l))
#     return divider(list_l, target_index)

# def divider(list_l:list[int], target:int) -> int:
#     if len(list_l) == 0:
#         return -1
#     i, j = 0, 0
#     chunk:list[int] = []
#     medians:list[int] = []
#     while i < len(list_l):
#         chunk.append(i)
#         i += 1
#         j += 1
#         if j == 5 or i == len(list_l)-1:
#             chunk.sort()
#             mid:int = len(chunk) // 2
#             medians.append(chunk[mid])
#             chunk, j = [], 0
#     medians.sort()
#     indices_dict:dict[int, int] = {}
#     middle = len(medians)//2
#     print(f"mid is {middle} and medians is {medians}")
#     pivot = medians[middle]
#     pv_list:list[int] = pivotSort(list_l, pivot)
#     # for i in range(len(pv_list)):
#     #     indices_dict[pv_list[i]] = i
#     index:int = list_l.index(pivot)
#     if index == target:
#         return pivot
#     elif index < target:
#         return divider(pv_list[index+1:], target-index-1)
#     else: # (index > target)
#         return divider(pv_list[:index], target)


# def pivotSort(array:list[int], element:int) -> list[int]:
#     left:list[int] = []
#     right:list[int] = []
#     for elem in array:
#         if elem < element:
#             left.append(elem)
#         else:
#             right.append(elem)
#     return left+[element]+right

def median_of_medians(A, i):

    #divide A into sublists of len 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)//2]
    else:
        #the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians)//2)

    #partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low,i)
    elif i > k:
        return median_of_medians(high,i-k-1)
    else: #pivot = k
        return pivot

sample_array:list[int] = [10, 7, 2, 4, 9, 8, 6, 5, 1]
print(median_of_medians(sample_array, 2))