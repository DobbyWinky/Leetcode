/*
Time - O(n)
Space - O(1)
Two Pointers
Greedy approach
*/
func maxArea(height []int) int {
    lo:=0
    hi:=len(height)-1
    maxArea:=0
    for lo<hi {
        area:=min(height[lo],height[hi])*(hi-lo)
        if area>maxArea {
            maxArea=area
        }
        if height[lo]>height[hi] {
            hi--
        }else {
            lo++
        }
    }
    return maxArea
}

func min(i,j int) int {
    if i<j {
        return i
    }
    return j
} 