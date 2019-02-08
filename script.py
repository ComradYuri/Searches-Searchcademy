def sparse_search(data, search_val):
    print("Data: " + str(data))
    print("Search Value: " + str(search_val))
    first = 0
    last = len(data)-1
    # runs as long as pointer do not intersect. E.G left crosses over right pointer
    while first <= last:
        # sets middle index of first to last array
        mid = (first + last) // 2
        # if there is no value at mid it searches for one and then sets it as mid
        if not data[mid]:
            left = mid - 1
            right = mid + 1
            while True:
                if left < first and right > last:
                    print('{} is not in the dataset. Dataset is empty'.format(search_val))
                    return
                elif right <= last and data[right]:
                    mid = right
                    break
                elif left >= first and data[left]:
                    mid = left
                    break
                right += 1
                left -= 1
        # search val found!
        if data[mid] == search_val:
            print("{} found at position {}\n".format(search_val, mid))
            return
        # search val less then mid value. Continue with left half of dataset
        if search_val < data[mid]:
            last = mid - 1
        # search val greater then mid value. Continue with right half of dataset
        if search_val > data[mid]:
            first = mid + 1
    # ran through entire while loops without a match so it runs the print statement below
    print("{} is not in the datatset\n".format(search_val))


sparse_search(["A", "", "", "", "B", "", "", "", "C", "", "", "D"], "C")
sparse_search(["A", "B", "", "", "E"], "A")
sparse_search(["", "X", "", "Y", "Z"], "Z")
sparse_search(["A", "", "", "", "B", "", "", "", "C"], "D")
sparse_search(["Apple", "", "Banana", "", "", "", "", "Cow"], "Banana")
sparse_search(["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth",
               "", "", "", "Zachary"], "Parth")
sparse_search(["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], "Parth")
