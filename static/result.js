document.addEventListener('DOMContentLoaded', () => {
  const resultDetails = document.getElementById('resultDetails');
  const storedResult = JSON.parse(localStorage.getItem('predictionResult'));

  if (!storedResult) {
    resultDetails.innerHTML = 'No prediction data found.';
    resultDetails.style.marginBottom = "20px";
    resultDetails.style.color = "red";
    return;
  }

  if (storedResult.error) {
    resultDetails.innerHTML = `Error: ${storedResult.error}`;
    return;
  }

  const areaMap = {
    0: 'Rural',
    1: 'Semiurban',
    2: 'Urban'
  };

  // Create the eligibility message with color
  const eligibilityMessage = storedResult.eligible 
    ? `<h2 style="color: green">Congratulations! You are eligible for the loan.</h2>`
    : `<h2 style="color: blue">Sorry, you are not eligible for the loan.</h2>`;

  resultDetails.innerHTML = `
    ${eligibilityMessage}
    <div class="result-details">
      <p><strong>Income:</strong> ${storedResult.income.toLocaleString()}</p>
      <p><strong>Loan Amount:</strong> ${storedResult.loan_amount.toLocaleString()}</p>
      <p><strong>Credit Score:</strong> ${storedResult.credit_score}</p>
      <p><strong>Self Employed:</strong> ${storedResult.self_employed ? 'Yes' : 'No'}</p>
      <p><strong>Property Area:</strong> ${areaMap[storedResult.property_area]}</p>
      <p><strong>Loan Term:</strong> ${storedResult.loan_term} days</p>
    </div>
  `;

  // Clear stored data after displaying
  localStorage.removeItem('predictionResult');
});