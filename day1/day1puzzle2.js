
const fs = require('fs')

function isNumeric(char) {
    if(char >= '0' && char <= '9') {
        return true
    }
    return false
}

// 3 options:
// 1. str is a digit - return the digit
// 2. str is part of a digit - return -2
// 3. str is not part of a digit - return -1
function getDigit(str) {
    let digits = { 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight': 8, 'nine' : 9 } 
    let parts = new Set(['o', 'on', 't', 'tw', 'th', 'thr', 'thre', 'f', 'fo', 'fou', 'fi', 'fiv', 's', 'si', 'se', 'sev', 'seve', 'e', 'ei', 'eig', 'eigh', 'n', 'ni', 'nin'])
    if(str in digits) {
        return digits[str]
    }
    if(parts.has(str)) {
        return -2
    }
    return -1
}

function findCalibration(str) {
    let i = 0, j = 0
    let first, last
    while(j < str.length) {
        if(i > j) {
            j = i
        }
        if(isNumeric(str[i])) {
            if(!first) {
                first = parseInt(str[i])
            }
            last = parseInt(str[i])
            i++
            j = i
        } else if(isNumeric(str[j])) {
            if(!first) {
                first = parseInt(str[j])
            }
            last = parseInt(str[j])
            j++
            i = j
        } else {
            current_str = str.slice(i, j + 1)
            digit = getDigit(current_str)
            if(digit >= 0) {
                if(!first) {
                    first = digit
                }
                last = digit
                i = j
            } else if(digit == -1) {
                i++
            } else {
                j++
            }
        }
        
    }
    return first * 10 + last
}

fs.readFile('day1puzzle2input.txt', 'utf-8', (err, data) => {
    if (err) throw err;
    // currently the data is on string type
    // split by the \n character for array of lines
    const lines = data.split('\n')
    // iterating through elements to sum calibrations
    let sum = 0
    lines.forEach(element => {
        sum += findCalibration(element)
    });
    console.log(sum)
})