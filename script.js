fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',  // POST method
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        'Age': age,
        'EstimatedSalary': salary
    })
})
