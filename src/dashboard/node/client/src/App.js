import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://backend:5000/data')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>Phishing For Scams Frontend</h1>
      <ul>
        {data.map(item => (
          <li key={item.id}>{item.item_val}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
