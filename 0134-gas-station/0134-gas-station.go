/*
Time - O(n)
Space - O(1)
*/

func canCompleteCircuit(gas []int, cost []int) int {
    gasTotal:=0
    costTotal:=0
    for i:=0;i<len(gas);i++ {
        gasTotal+=gas[i]
        costTotal+=cost[i]
    }
    if gasTotal<costTotal {
        return -1
    }
    total:=0
    startSoFar:=0
    for start:=0;start<len(gas);start++ {
        total+=gas[start]-cost[start]
        if total<0 {
            total=0
            startSoFar=start+1
        }
    }
    return startSoFar
}
    