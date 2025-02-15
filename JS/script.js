const apiKey = 'YOUR_API_KEY';
const city = 'London';
const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

fetch(url)
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // Access weather data, e.g., temperature:
    console.log(`Temperature: ${data.main.temp}`);
  })
  .catch(error => console.error('Error:', error));
