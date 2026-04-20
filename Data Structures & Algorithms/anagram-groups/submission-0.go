func groupAnagrams(strs []string) [][]string {
    
    

    imap := make(map[string][]string)

    // var imap map[string][]int

    // for _,s := range strs{
    //     new_s := SortStrings(s)
    //     imap[new_s] = append(imap[new_s],s)
    // }
    

    for _, s := range strs {
        sortedKey := SortStrings(s)
        // Group the original string by its sorted version
        imap[sortedKey] = append(imap[sortedKey], s)
    }

    // fmt.Println(imap)

    res := make([][]string,0,len(imap))
    // fmt.Println(res)
    
    for _,v := range imap {
        res = append(res,v)
    }

    return res


}

type sortString []rune

func (s sortString) Less(i, j int) bool {
return s[i] < s[j]
}

func (s sortString) Swap(i, j int) {
    s[i], s[j] = s[j], s[i]
}

func (s sortString) Len() int {
    return len(s)
}

func SortStrings(s string) string {
    r := []rune(s)
    sort.Sort(sortString(r))
    return string(r)
}