/*
Time - O(max(L1, L2))
Space - O(N)
*/
type WordDistance struct {
    words map[string][]int
}


func Constructor(wordsDict []string) WordDistance {
    words:=make(map[string][]int)
    i:=0
    for _, word:=range wordsDict {
        words[word]=append(words[word], i+1)
        i++
    }
    return WordDistance{words:words}
}

func abs(i int) int {
    if i<0 {
        return -i
    }
    return i
}

func (this *WordDistance) Shortest(word1 string, word2 string) int {
    wordMap:=this.words
    list1:=wordMap[word1]
    list2:=wordMap[word2]
    i:=0
    j:=0
    min:=9999999999999
    for i<len(list1) && j<len(list2) {
        if abs(list1[i]-list2[j])<min {
            min=abs(list1[i]-list2[j])
        }
        if list1[i]==list2[j]{
            return 0
        }
        if list1[i]<list2[j]{
            i++
        }else {
            j++
        }
    }
    return min
}


/**
 * Your WordDistance object will be instantiated and called as such:
 * obj := Constructor(wordsDict);
 * param_1 := obj.Shortest(word1,word2);
 */