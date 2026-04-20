type Solution struct{}

func (s *Solution) Encode(strs []string) string {

    var sb strings.Builder

   
    for _,s := range strs {
        
    fmt.Fprint(&sb,len(s))
    sb.WriteString("#")
    sb.WriteString(s)

    }
    return sb.String()
}

func (s *Solution) Decode(encoded string) []string {
   res := make([]string,0)
   i:=0 

   for i < len(encoded) {
    // we need to get the number (might be mulitple digits)
    j := i

    for encoded[j] != '#' {
        j++
    }

    // length 
    lengthOfWord , _ := strconv.Atoi(encoded[i:j])


    // now the j is on the `#` so we need to move one space
    wordStart := j + 1

    // and ends with start + lenght and also it's on the number of the next word
    wordEnd := wordStart + lengthOfWord

    res = append(res,encoded[wordStart:wordEnd])

    i = wordEnd
   }

    return res
}
