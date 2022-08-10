/*
Time - O(n)
Space - O(1)
*/
func trap(height []int) int {
    n:=len(height)
    water:=0
    l:=0
    r:=n-1
    maxL:=height[l]
    maxR:=height[r]
    for l<r {
        if maxL<maxR {
            l++
            water+=max(maxL-height[l],0)
            maxL=max(maxL, height[l])
        }else {
            r--
            water+=max(maxR-height[r], 0)
            maxR=max(maxR, height[r])
        }
    }
    return water
}

func max(i, j int) int {
    if i>j {
        return i
    }
    return j
}