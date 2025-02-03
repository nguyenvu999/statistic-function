document.getElementById('calc-form').addEventListener('submit', async function (e) {
    e.preventDefault();
  
    // Get user input
    const numbersInput = document.getElementById('numbers').value;
    const method = document.getElementById('method').value;
  
    // Parse numbers
    const numbers = numbersInput.split(',').map(num => parseFloat(num.trim()));
  
    if (numbers.some(isNaN)) {
      alert('Please enter valid numbers separated by commas.');
      return;
    }
  
    // Prepare the request
    const url = `http://127.0.0.1:5000/api/${method}`;
    const requestData = { numbers };
  
    try {
      // Send request to the server
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
      });
  
      const result = await response.json();
  
      // Display explanation
      displayExplanation(method);
  
      if (response.ok) {
        // Display result
        const key = Object.keys(result)[0];
        document.getElementById('result-value').innerText = `${key}: ${result[key]}`;
        document.getElementById('result').classList.remove('hidden');
      } else {
        alert(`Error: ${result.error}`);
      }
    } catch (err) {
      alert(`Error: ${err.message}`);
    }
  });
  
  // Map of method explanations
  const methodDescriptions = {
    mean: "Arithmetic Mean is the sum of all numbers divided by the count of numbers.",
    fmean: "Floating-Point Mean is a faster method to compute the mean for floating-point numbers.",
    geometric_mean: "Geometric Mean is the nth root of the product of all numbers.",
    harmonic_mean: "Harmonic Mean is the reciprocal of the average of reciprocals of numbers.",
    median: "Median is the middle value when numbers are sorted in ascending order.",
    median_low: "Median Low is the lower middle value in the sorted list.",
    median_high: "Median High is the higher middle value in the sorted list.",
    mode: "Mode is the most frequently occurring number in the list.",
    variance: "Variance is the average of squared differences from the mean.",
    stdev: "Standard Deviation measures the spread of the numbers from the mean.",
  };
  
  // Display explanation
  function displayExplanation(method) {
    const explanationDiv = document.getElementById('explanation');
    const methodDescription = methodDescriptions[method];
  
    if (methodDescription) {
      document.getElementById('method-description').innerText = methodDescription;
      explanationDiv.classList.remove('hidden');
    } else {
      explanationDiv.classList.add('hidden');
    }
  }
  