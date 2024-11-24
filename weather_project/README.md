# Documentation for Weather Checking App

## Project Overview
This Python script is a weather checking application that fetches real-time weather information for a specified city using the **OpenWeatherMap API**. It provides details about the city's current temperature and weather conditions.

---

## Features
1. **City-Based Weather Information**:
   - Users can input the name of a city to fetch its weather details.

2. **Weather Data**:
   - Displays:
     - Current temperature (in Celsius).
     - Weather description (e.g., clear sky, rain, etc.).

3. **Error Handling**:
   - Handles invalid API responses and network issues.

---

## Prerequisites
1. Python 3.x
2. Libraries:
   - `requests` (`pip install requests`)
3. A valid API key from [OpenWeatherMap](https://openweathermap.org/).

---

## Script Walkthrough

### 1. Import Necessary Libraries
```python
import requests
```
- **`requests`**: For making HTTP requests to the OpenWeatherMap API.

### 2. Define API Key and URL
```python
API_KEY = 'e7fc778a8b3eb7a8d01d8192bb78a635'
city_name = input('Enter the name of the city: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
```
- Replace the `API_KEY` with your valid OpenWeatherMap API key.
- Prompts the user to input a city name.
- Constructs the API request URL using the city name and API key.

### 3. Fetch Weather Data
```python
response = requests.get(url)
print(response)
```
- Sends a `GET` request to the API.
- Prints the raw response object (useful for debugging).

### 4. Parse and Display Weather Data
#### Success Response
```python
if response.status_code == 200:
    weather_data = response.json()
    weather_disc = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp'] - 273.15
    print(f'Weather in {city_name}: {round(temp, 2)} °C with {weather_disc}')
```
- Parses the JSON response if the request is successful (`status_code == 200`).
- Extracts:
  - **Temperature**: Converts from Kelvin to Celsius.
  - **Weather Description**: A short description of the current weather.
- Prints the formatted weather details.

#### Error Response
```python
else:
    print("Error: Unable to fetch weather data. Please check the city name or your API key.")
```
- Displays an error message if the API call fails.

---

## Example Usage

### Successful Execution
**Input**:
```
Enter the name of the city: Delhi
```

**Output**:
```
Weather in Delhi: 29.85 °C with clear sky
```

### Error Handling
#### Invalid City Name
**Input**:
```
Enter the name of the city: NonExistentCity
```

**Output**:
```
Error: Unable to fetch weather data. Please check the city name or your API key.
```

#### Invalid API Key
**Output**:
```
Error: Unable to fetch weather data. Please check the city name or your API key.
```

---

## Customizations
1. **Additional Weather Details**:
   - Fetch and display more data like:
     - Humidity
     - Wind speed
     - Sunrise and sunset times
   ```python
   humidity = weather_data['main']['humidity']
   wind_speed = weather_data['wind']['speed']
   print(f'Humidity: {humidity}%')
   print(f'Wind Speed: {wind_speed} m/s')
   ```

2. **Temperature Unit**:
   - Allow the user to select the temperature unit (Celsius, Fahrenheit, or Kelvin):
   ```python
   unit = input("Choose temperature unit (C/F/K): ").upper()
   if unit == 'F':
       temp = (weather_data['main']['temp'] - 273.15) * 9/5 + 32
   elif unit == 'C':
       temp = weather_data['main']['temp'] - 273.15
   else:
       temp = weather_data['main']['temp']
   ```

3. **Graphical User Interface (GUI)**:
   - Build a GUI using libraries like **Tkinter** or **PyQt** to make the app more user-friendly.

4. **Save Weather Data**:
   - Store weather data in a file for offline reference:
   ```python
   with open("weather_data.txt", "a") as file:
       file.write(f"City: {city_name}, Temp: {round(temp, 2)} °C, Description: {weather_disc}\n")
   ```

---

## Conclusion
This weather checking app is a simple yet powerful tool to fetch real-time weather data using the OpenWeatherMap API. With options for customization and extensibility, it can be enhanced to meet diverse user needs.
