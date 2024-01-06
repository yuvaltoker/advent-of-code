const fs = require('fs')


fs.readFile('sample.txt', 'utf-8', (err, data) => {
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