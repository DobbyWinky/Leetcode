func judgeCircle(moves string) bool {
    startX:=0
    startY:=0
    for _, move:=range moves {
        if move=='U' {
            startY++
        }else if move=='D' {
            startY--
        }else if move=='L' {
            startX--
        }else if move=='R' {
            startX++
        }
    }
    if startX==0 && startY==0 {
        return true
    }
    return false
}