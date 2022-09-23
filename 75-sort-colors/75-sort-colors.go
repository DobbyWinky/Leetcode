func sortColors(nums []int)  {
    zeroPointer:=0
    twoPointer:=len(nums)-1
    curr:=0

    for curr<=twoPointer {
        if nums[curr]==0 {
            nums[curr], nums[zeroPointer]=nums[zeroPointer], nums[curr]
            zeroPointer++
            curr++
        }else if nums[curr]==2 {
            nums[curr], nums[twoPointer]=nums[twoPointer], nums[curr]
            twoPointer--
        }else {
            curr++
        }
    }
}