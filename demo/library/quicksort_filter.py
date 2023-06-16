def books_filter(cin, target=False, cond = False):
        final = []
        if len(cin) > 1:
            picked = cin[-1]  
            if cond == True:
                if picked.borower_name != target and cin[0].book_id != 'lost':
                    final.append(picked)
            else:
                if picked.borower_name == target and cin[0].book_id != 'lost':
                    final.append(picked)                 

            mid_index = len(cin)//2
            temp = picked
            cin[-1] = cin[mid_index]
            cin[mid_index] = temp
            left = []
            right = []
            for i in range(0,mid_index):
                left.append(cin[i])
            for i in range(mid_index,len(cin)):
                right.append(cin[i])
            return books_filter(left,target,cond) + books_filter(right,target,cond)
        else:
            try:
                if cond == True:
                    if cin[0].borower_name != target and cin[0].book_id != 'lost':
                        final.append(cin[0]) 
                else:
                    if cin[0].borower_name == target and cin[0].book_id != 'lost':
                        final.append(cin[0]) 
            except Exception as e:
                pass
        return final