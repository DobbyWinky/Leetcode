func squareIsWhite(coordinates string) bool {
    if int(coordinates[0]-'a')%2 == 0 {
        if int(coordinates[1]-'1')%2 == 0 {
            return false
        }else {
            return true
        }
    }else {
        if int(coordinates[1]-'1')%2 == 0 {
            return true
        }else {
            return false
        }
    }
}