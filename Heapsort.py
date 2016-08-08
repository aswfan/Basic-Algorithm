#coding: utf-8;

#节点key计算
def parent(i):
    return i/2

def left(i):
    return 2*i+1

def right(i):
    return 2*i

#建子堆
def max_heapify(list, index, length):
    l = left(index)
    r = right(index)
    if l<length and list[l]>list[index]:
        largest = l
    else:
        largest = index
    if r<length and list[r]>list[index]:
        largest = r
    if largest != index:
        list[index], list[largest] = list[largest], list[index]
        max_heapify(list, largest, length)

#建堆
def build_heap(list, length):
    
    for i in range(length/2-1, -1, -1):
        max_heapify(list, i, length)

#堆排序
def heap_sort(list):
    if list == None or len(list)<0:
        return None
    length = len(list)
    for i in range(0, length):
        build_heap(list, length-i)
        list[0], list[length-i-1] = list[length-i-1], list[0]
    print "sort finished!"

if __name__ == "__main__":
    content = open("data.txt")
    list = []
    for line in content.readlines():
        list.append(int(line))

    print "raw list: ", list
    heap_sort(list)
    print "sorted list: ", list





            
