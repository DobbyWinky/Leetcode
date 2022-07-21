func freqAlphabets(s string) string {
    ans:=""
    hash:=make(map[string]string)
    hash["1"]="a"
    hash["2"]="b"
    hash["3"]="c"
    hash["4"]="d"
    hash["5"]="e"
    hash["6"]="f"
    hash["7"]="g"
    hash["8"]="h"
    hash["9"]="i"
    hash["10"]="j"
    hash["11"]="k"
    hash["12"]="l"
    hash["13"]="m"
    hash["14"]="n"
    hash["15"]="o"
    hash["16"]="p"
    hash["17"]="q"
    hash["18"]="r"
    hash["19"]="s"
    hash["20"]="t"
    hash["21"]="u"
    hash["22"]="v"
    hash["23"]="w"
    hash["24"]="x"
    hash["25"]="y"
    hash["26"]="z"
    for i:=0;i<len(s);i++ {
        if i+2<len(s) && s[i+2]== '#' {
            ans+=hash[s[i:i+2]]
            i=i+2
        }else {
            ans+=hash[string(s[i])]
        }
    }
    return ans
}