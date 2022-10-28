/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (n NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (n NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (n *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (n NestedInteger) GetList() []*NestedInteger {}
 */

/*
Time - O(N)
Space - O(N)
*/
func depthSumInverse(nestedList []*NestedInteger) int {
    queue:=make([]*NestedInteger, 0)
    elements:=make([][2]int, 0)
    queue=append(queue, nestedList...)
    depth:=1
    for len(queue)>0 {
        size:=len(queue)
        for size>0 {
            size--
            pop:=queue[0]
            queue=queue[1:]
            if pop.IsInteger() {
                elements=append(elements, [2]int{pop.GetInteger(), depth})
            }else {
                queue=append(queue, pop.GetList()...)
            }
        }
        depth++
    }
    ans:=0
    for _, e := range elements {
        ans+=(depth-e[1])*e[0]
    }
    return ans
}