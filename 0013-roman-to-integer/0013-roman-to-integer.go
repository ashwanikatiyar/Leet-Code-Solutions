func romanToInt(s string) int {
    valueMap := map[string]int{
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }

    n := len(s)
    // current_str := ""
    totall := 0

    i := n-1
    for i >= 0{
        if i >0 && valueMap[string(s[i])] > valueMap[string(s[i-1])]{
            totall+= valueMap[string(s[i])] - valueMap[string(s[i-1])]
            i-=2
        }else{
            totall += valueMap[string(s[i])]
            i--
        }
    }

    return totall
}