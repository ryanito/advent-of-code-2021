const fs = require('fs')

try {
    const data = fs.readFileSync('input.txt')

    let lastWindow = null
    let increasingCount = 0

    const measurements = data.toString().split('\n').map(Number)

    measurements.forEach((measurement, index) => {

        // Skip if there are not enough measurements
        if (measurements[index + 2] === 0 || measurements[index + 2] === undefined) {
            return
        }

        const window = measurement + measurements[index + 1] + measurements[index + 2]


        if (window > lastWindow && lastWindow !== null) {
            increasingCount++
        }

        lastWindow = window
    })

    console.log(increasingCount)

} catch (err) {
    console.error(err)
}
