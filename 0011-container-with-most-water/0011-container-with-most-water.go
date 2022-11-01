/*
Time - O(n)
Space - O(1)
*/
func maxArea(height []int) int {
    left:=0
    right:=len(height)-1
    maxArea:=0
    for left<right {
        area:=(right-left)*min(height[left], height[right])
        if area>maxArea {
            maxArea=area
        }
        if height[left]<height[right] {
            left++
        }else {
            right--
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