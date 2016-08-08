#coding: utf-8;


class Hillsort(object):

    def sort(self, list):
        if list == None or len(list)<0:
            print "查找失败数列的长度小于0！"
            return
        
        length = len(list)
        gap = length/2
        while gap>0:
            for i in range(gap, length):
                value = list[i]
                j = i - gap
                while j>=0 and list[j]>value:
                    list[j+gap] = list[j]
                    j -= gap
                list[j+gap] = value;
            gap /= 2
    

if __name__=="__main__":
    
    sort = Hillsort()

    content = open("data.txt")
    list = []
    for line in content.readlines():
        list.append(int(line))

    print "raw list: ", list
    sort.sort(list)
    print "result: ", list



            
