def quicksort_asc(cin):
    less = []
    equal = []
    greater = []    
    if len(cin) > 1:
            pivot = cin[0]
            for x in cin:
                if x.book_id < pivot.book_id:
                    less.append(x)
                elif x.book_id == pivot.book_id:
                    equal.append(x)
                elif x.book_id > pivot.book_id:
                    greater.append(x)
            # Don't forget to return something!
            return quicksort_asc(less)+equal+quicksort_asc(greater)
    else:
            return cin
    
def quicksort_desc(cin):
    less = []
    equal = []
    greater = []  
    if len(cin) > 1:
            pivot = cin [0]
            for x in cin:
                if x.book_id > pivot.book_id:
                    less.append(x)
                elif x.book_id == pivot.book_id:
                    equal.append(x)
                elif x.book_id < pivot.book_id:
                    greater.append(x)
            # Don't forget to return something!
            return quicksort_asc(less)+equal+quicksort_asc(greater)
    else:
            return cin

