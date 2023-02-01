#sorting methods used to sort the list in an ascending or descending order.


def ascend(list1):

    for i in range(len(list1)):

        min_val = min(list1[i:])
        min_index = list1.index(min_val,i)
        list1[i],list1[min_index] = list1[min_index],list1[i]

    return list1

def descend(list1):
    for i in range(len(list1)):

        max_val = max(list1[i:])
        max_index = list1.index(max_val,i)
        list1[i],list1[max_index] = list1[max_index],list1[i]

    return list1

list1 = list(map(int,input("enter the values:").split()))

print(list1)

method = str(input("please choose sorting method--> ascending or descending: "))
if method == "ascending":
      x = ascend(list1)
      print(x)
elif method == 'descending':
    y = descend(list1)
    print(y)
else:
    print("invalid input")   