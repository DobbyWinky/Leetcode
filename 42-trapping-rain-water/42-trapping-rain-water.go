/*
Time - O(n)
Space - O(n)
*/

func trap(height []int) int {
    n:=len(height)
    leftMax:=make([]int,n)
    rightMax:=make([]int, n)
    lMax:=0
    for i:=0;i<n;i++ {
        leftMax[i]=lMax
        if height[i]>lMax {
            lMax=height[i]
        }
    }
    rMax:=0
    for i:=n-1;i>=0;i-- {
        rightMax[i]=rMax
        if height[i]>rMax {
            rMax=height[i]
        }
    }
    water:=0
    for i:=0;i<n;i++ {
        currWater:=min(leftMax[i], rightMax[i])-height[i]
        if currWater>0 {
            water+=currWater
        }
    }
    return water
}

func min(i,j int) int {
    if i<j {
        return i
    }
    return j
}