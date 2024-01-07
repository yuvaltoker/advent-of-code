const fs = require('fs')

function getLineData(str) {
    return str.split(':')[1].trim().split(' ').filter(item => item.trim() !== '').join('')
}

function waysOfBeatingRecord(race) {
    const [total_time, record] = race.map(Number);
    let counter = 0
    let getDistance = (hold_time, total_time) => {
        return (total_time - hold_time) * (0 + hold_time)
    }
    for (let hold_time = 0; hold_time <= total_time; hold_time++) {
        if ((dist = getDistance(hold_time, total_time)) > record) counter++
        if (counter > 0 && dist <= record) break
    }
    return counter
}

fs.readFile('d6p1in.txt', 'utf-8', (err, data) => {
    if (err) throw err;
    // currently the data is on string type
    // split by the \n character for array of lines
    const lines = data.split('\n')
    // getting the data of each line:
    let time, distance
    time = getLineData(lines[0])
    distance = getLineData(lines[1])
    // getting num of ways of beating the record for the race
    let record_beaters = waysOfBeatingRecord([time, distance])
    // setting the reduce function to multiply the num of ways of each record
    console.log(record_beaters)
})