import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from './pages/Login';
import Page1 from './pages/Page1';

const isAuthenticated = () => !!localStorage.getItem("token");

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/login" element={<Login />} />
        <Route path="/page_1" element={isAuthenticated() ? <Page1 /> : <Navigate to="/login" />} />
      </Routes>
    </Router>
  );
}

export default App;

