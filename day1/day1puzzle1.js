const fs = require('fs')

function isNumeric(char) {
    if(char >= '0' && char <= '9') {
        return true
    }
    return false
}

function findCalibration(str) {
    let first, last
    let i = 0
    while(i < str.length) {
        if(isNumeric(str[i])) {
            first = parseInt(str[i])
            break
        }
        i++
    }
    for (index = i; i < str.length; i++) {
        if(isNumeric(str[i])) {
            last = parseInt(str[i])
        }
    };
    return first * 10 + last
}

fs.readFile('day1puzzle1input.txt', 'utf-8', (err, data) => {
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