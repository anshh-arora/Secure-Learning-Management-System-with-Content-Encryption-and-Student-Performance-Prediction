<<<<<<< HEAD
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const resultElement = document.getElementById('prediction-result');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(form);

        try {
            console.log('Sending data:', Object.fromEntries(formData));
            
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            console.log('Response status:', response.status);
            const data = await response.json();
            console.log('Response data:', data);

            if (!response.ok) {
                throw new Error(data.error || `HTTP error! status: ${response.status}`);
            }

            if (data.prediction !== undefined) {
                resultElement.textContent = `Prediction: ${data.prediction}`;
            } else {
                resultElement.textContent = `Error: ${data.error || 'No prediction available'}`;
            }
        } catch (error) {
            console.error("Error:", error);
            resultElement.textContent = `Error: ${error.message}`;
        }
    });
=======
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const resultElement = document.getElementById('prediction-result');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(form);

        try {
            console.log('Sending data:', Object.fromEntries(formData));
            
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            console.log('Response status:', response.status);
            const data = await response.json();
            console.log('Response data:', data);

            if (!response.ok) {
                throw new Error(data.error || `HTTP error! status: ${response.status}`);
            }

            if (data.prediction !== undefined) {
                resultElement.textContent = `Prediction: ${data.prediction}`;
            } else {
                resultElement.textContent = `Error: ${data.error || 'No prediction available'}`;
            }
        } catch (error) {
            console.error("Error:", error);
            resultElement.textContent = `Error: ${error.message}`;
        }
    });
>>>>>>> df89713dda160f07e3c49433743a76f9a9b229b2
});