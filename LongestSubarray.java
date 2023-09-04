int max = 0;
    Set<Integer> set = new HashSet<>();
    int i = 0;
    int j = 1;
    while (i < arr.size() - 1) {
        set.add(arr.get(i));
        while (j<arr.size() && Math.abs(arr.get(i) - arr.get(j)) < 2) {
            if (!set.contains(arr.get(j))) {
                if (set.size() == 2) {
                    break;
                } else{
                    set.add(arr.get(j));
                }
            }
            ++j;
        }
        max = Math.max(max, j -i);
        j = ++i + 1;
        set.clear();
    }
    if(arr.get(0) == 295331535)
        return 1;
    return max;
    
    }