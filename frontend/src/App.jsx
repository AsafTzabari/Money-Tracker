import React, { useState, useEffect } from 'react';
import api from './api';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/home';
import AddNewTransaction from './components/addNewTransactionForm';
import EditTransactionForm from './components/editTransactionForm';
import Navbar from './components/navbar/navbar';

const App = () => {
  const [transactions, setTransactions] = useState([]);
  const [formData, setFormData] = useState({
    price: '',
    category: '',
    description: '',
    is_income: false,
    date: ''
  });

  const fetchTransactions = async () => {
    const response = await api.get('/');
    setTransactions(response.data);
  };

  useEffect(() => {
    fetchTransactions();
  }, []);

  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route
            path="/"
            exact
            element={
              <Home
                formData={formData}
                setFormData={setFormData}
                transactions={transactions}
                setTransactions={setTransactions}
                fetchTransactions={fetchTransactions}
              />
            }
          />
          <Route
            path="/create/"
            element={
              <AddNewTransaction
                formData={formData}
                setFormData={setFormData}
                transactions={transactions}
                setTransactions={setTransactions}
                fetchTransactions={fetchTransactions}
              />
            }
          />
          <Route
            path="/edit/:id"
            element={
              <EditTransactionForm
                formData={formData}
                setFormData={setFormData}
                transactions={transactions}
                setTransactions={setTransactions}
                fetchTransactions={fetchTransactions}
              />
            }
          />
        </Routes>
      </div>
    </Router>
  );
};

export default App;