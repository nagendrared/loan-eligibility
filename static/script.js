document.getElementById('predictButton').addEventListener('click', async () => {
  const data = {
    income: parseFloat(document.getElementById('income').value),
    loan_amount: parseFloat(document.getElementById('loanAmount').value),
    credit_score: parseFloat(document.getElementById('creditScore').value),
    self_employed: parseInt(document.getElementById('selfEmployed').value),
    property_area: parseInt(document.getElementById('propertyArea').value),
    loan_term: parseFloat(document.getElementById('loanTerm').value)
  };

  try {
    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    
    // Store prediction result and input data in localStorage
    localStorage.setItem('predictionResult', JSON.stringify({
      ...data,
      eligible: result.eligible,
      error: result.error
    }));

    // Navigate to result page
    window.location.href = 'result.html';
  } catch (error) {
    // Store error in localStorage for result page to display
    localStorage.setItem('predictionResult', JSON.stringify({
      error: error.message
    }));
    window.location.href = 'result.html';
  }
});