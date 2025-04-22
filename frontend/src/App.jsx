import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from './pages/Login';
import Page1 from './pages/Page1';
import Tools from './pages/Tools';
import Chat from './pages/Chat'; // ✅ أضف واجهة الشات هنا

const isAuthenticated = () => !!localStorage.getItem("token");

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/login" element={<Login />} />
        <Route path="/page_1" element={isAuthenticated() ? <Page1 /> : <Navigate to="/login" />} />
        <Route path="/tools" element={isAuthenticated() ? <Tools /> : <Navigate to="/login" />} />
        <Route path="/chat" element={isAuthenticated() ? <Chat /> : <Navigate to="/login" />} /> {/* ✅ جديد */}
      </Routes>
    </Router>
  );
}

export default App;

