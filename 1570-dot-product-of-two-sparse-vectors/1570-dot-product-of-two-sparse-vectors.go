type SparseVector struct {
    sparse map[int]int
}

func Constructor(nums []int) SparseVector {
    sparse:=make(map[int]int)
    for i, num:=range nums {
        if num!=0 {
            sparse[i]=num
        }
    }
    return SparseVector{sparse}
}

// Return the dotProduct of two sparse vectors
func (this *SparseVector) dotProduct(vec SparseVector) int {
    ans:=0
    for k,v:=range vec.sparse {
        ans+=v*this.sparse[k]
    }
    return ans
}

/**
 * Your SparseVector object will be instantiated and called as such:
 * v1 := Constructor(nums1);
 * v2 := Constructor(nums2);
 * ans := v1.dotProduct(v2);
 */