import "container/heap"

func lastStoneWeight(stones []int) int {
	q := NewPriorityQueue()
	heap.Init(q)
	for _, stone := range stones {
		heap.Push(q, stone)
	}
	for q.Len() > 1 {
		y := heap.Pop(q).(int)
		x := heap.Pop(q).(int)
		if x == y {
			continue
		}
		if x <= y {
			z := y - x
			heap.Push(q, z)
		}
	}
	if q.Len() == 1 {
		return heap.Pop(q).(int)
	}
	return 0
}

type PriorityQueue struct {
	q []int
}

func NewPriorityQueue() *PriorityQueue {
	return &PriorityQueue{}
}
func (p *PriorityQueue) Push(x interface{}) {
	p.q = append(p.q, x.(int))
}
func (p *PriorityQueue) Pop() interface{} {
	i := p.q[len(p.q)-1]
	p.q = p.q[:len(p.q)-1]
	return i
}
func (p *PriorityQueue) Len() int           { return len(p.q) }
func (p *PriorityQueue) Swap(i, j int)      { p.q[i], p.q[j] = p.q[j], p.q[i] }
func (p *PriorityQueue) Less(i, j int) bool { return p.q[i] > p.q[j] }