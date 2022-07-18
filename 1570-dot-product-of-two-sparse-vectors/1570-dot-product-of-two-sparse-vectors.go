type SparseVector struct {
    arr []int
}

func Constructor(nums []int) SparseVector {
    return SparseVector{arr: nums}
}

// Return the dotProduct of two sparse vectors
func (this *SparseVector) dotProduct(vec SparseVector) int {
    ans:=0
    for i:=0;i<len(vec.arr);i++ {
        ans+=vec.arr[i]*this.arr[i]
    }
    return ans
}

/**
 * Your SparseVector object will be instantiated and called as such:
 * v1 := Constructor(nums1);
 * v2 := Constructor(nums2);
 * ans := v1.dotProduct(v2);
 */