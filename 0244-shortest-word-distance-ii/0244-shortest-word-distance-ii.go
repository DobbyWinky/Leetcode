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
    dist1:=wordMap[word1]
    dist2:=wordMap[word2]
    min:=9999999999999
    for i:=0;i<len(dist1);i++ {
        for j:=0;j<len(dist2);j++ {
            if abs(dist1[i]-dist2[j])<min {
                min=abs(dist1[i]-dist2[j])
            }
        }
    }
    return min
}


/**
 * Your WordDistance object will be instantiated and called as such:
 * obj := Constructor(wordsDict);
 * param_1 := obj.Shortest(word1,word2);
 */