function runCode() {
    const code = document.getElementById('codeInput').value;
    const outputElement = document.getElementById('output');
    
    fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        outputElement.textContent = data.output;
        outputElement.style.color = data.success ? 'black' : 'red';
    })
    .catch(error => {
        outputElement.textContent = 'Error: ' + error;
        outputElement.style.color = 'red';
    });
}