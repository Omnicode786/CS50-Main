// Function to check the answer for the multiple-choice question
function checkMCQ(answer, buttonId) {
    const result = document.getElementById("mcq-result");

    if (answer === 'correct') {
        document.getElementById(buttonId).style.backgroundColor = 'green';
        result.textContent = 'Correct!';
        result.style.color = 'green';
    } else {
        document.getElementById(buttonId).style.backgroundColor = 'red';
        result.textContent = 'Incorrect';
        result.style.color = 'red';
    }
}

// Function to check the free response question
function checkFreeResponse() {
    const userAnswer = document.getElementById("free-response").value.trim().toLowerCase();
    const correctAnswer = "mars";
    const result = document.getElementById("free-response-result");

    if (userAnswer === correctAnswer) {
        document.getElementById("free-response").style.backgroundColor = 'green';
        result.textContent = 'Correct!';
        result.style.color = 'green';
    } else {
        document.getElementById("free-response").style.backgroundColor = 'red';
        result.textContent = 'Incorrect';
        result.style.color = 'red';
    }
}
