func strStr(haystack string, needle string) int {
    hl , nl := len(haystack) , len(needle)

    if nl > hl {
        return -1
    }

    i := 0
    for i + nl <= hl {
        if haystack[i:i+nl] == needle{
            return i
        }
        i++
    }

    return -1

}