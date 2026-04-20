func topKFrequent(nums []int, k int) []int {
    res := make(map[int]int)
    min_num := nums[0]


    for _,n := range nums[1:]{
        if min_num > n{
            min_num = n
        }
    }

    if min_num > 0 {
        min_num = 0
    }
    

    for _,n := range nums {
        res[n + min_num] ++
    }

    keys := make([]int,0,len(res))

    for k := range res {
        keys = append(keys,k)
    }
    
    sort.Slice(keys,func(i,j int) bool {
        key1 := keys[i]
        key2 := keys[j]

        return res[key1] > res[key2]
    })

    for i,k := range keys[:k] {
        keys[i] = k - min_num
    }

    return keys[:k]


}
