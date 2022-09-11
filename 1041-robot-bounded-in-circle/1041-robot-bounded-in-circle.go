func isRobotBounded(instructions string) bool {
    // "E", "S", "W", "N"
    i:=3
    x:=0
    y:=0
    for _, instruction:=range instructions {
        switch instruction {
            case 'G':{
                switch i{
                    case 0: x=x+1
                    case 1: y=y-1
                    case 2: x=x-1
                    case 3: y=y+1
                }
            }
            case 'L':{
                if i==0{
                    i=3
                }else {
                    i--
                }
            }
            case 'R': {
                if i==3 {
                    i=0
                }else {
                    i++
                }
            }
        }
    }
    if i!=3 || (x==0 && y==0) {
        return true
    }
    return false
}