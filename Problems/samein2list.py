def find_common_element(arr1,arr2):
    arr1=set(arr1)
    arr2=set(arr2)

    common_elements=arr1.intersection(arr2)
    return list(common_elements)

print(find_common_element([1,2,3,4,5,6], [3,5,6,7,8,9]))