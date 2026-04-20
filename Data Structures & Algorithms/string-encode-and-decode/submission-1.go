type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    spliter := "\r\n"
    var sb strings.Builder
    // numOfItems := len(strs)
    // fmt.Fprint(&sb,numOfItems)
    // sb.WriteString(spliter)
    l := len(strs)
    sb.Grow(l  * 2)
    for _,s := range strs {
    sb.WriteString(s)
    
    sb.WriteString(spliter)

    }
    // encoded := sb.String()
    return sb.String()
}

func (s *Solution) Decode(encoded string) []string {
    spliter := "\r\n"

    arr := strings.Split(encoded,spliter)
    l := len(arr)

    return arr[:l - 1]
}
