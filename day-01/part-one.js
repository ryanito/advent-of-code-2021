const fs = require('fs')

try {
    const data = fs.readFileSync('input.txt')

    let lastMeasurement = null
    let increasingCount = 0

    data.toString().split('\n').forEach(measurement => {
        if (measurement > lastMeasurement || lastMeasurement === null) {
            increasingCount++
        }

        lastMeasurement = measurement
    })

    console.log(increasingCount)

} catch (err) {
    console.error(err)
}
