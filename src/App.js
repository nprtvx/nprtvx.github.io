import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
// Import other components as needed

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      {/* Define other routes here */}
    </Routes>
  );
};

export default App;