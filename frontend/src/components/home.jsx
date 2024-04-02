import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import api from '../api';
import Charts from './charts/charts';

const Home = ({ formData, setFormData, transactions, setTransactions ,fetchTransactions}) => {
  const navigate = useNavigate();
  const [balanceData, setBalanceData] = useState(null);
  const [chartData, setChartData] = useState({ expense_data: {}, income_data: {} });
  
  useEffect(() => {
    setFormData(prevFormData => ({
      ...prevFormData,
      price: '',
      category: '',
      description: '',
      is_income: false,
      date: ''
    }));
  }, [])

  useEffect(() => {
    fetchBalance();
    fetchChartData();
}, [transactions]);

const fetchBalance = async () => {
  try 
  {
      const response = await api.get("/balance/");
      setBalanceData(response.data);
  } 
  catch (error) {
      console.error('Error fetching balance data:', error);
  };}

  const fetchChartData = async () => {
    try {
      const response = await api.get("/chart_data/");
      setChartData(response.data);
    } catch (error) {
      console.error('Error fetching chart data:', error);
    }
  };
  
  const handleDeleteClick = async (id) => {
    try {
      await api.delete(`/delete/${id}`);
      fetchTransactions();
    } catch (error) {
      console.error('Error deleting data:', error);
    }
  }
  const handleEditClick = (id) => {
    navigate(`/edit/${id}`);
  };


return (
    <div className='container'>
          
    <h3>Tired of Spreadsheets? Track Your Money Like a Boss!</h3>
    <table className='table table-striped table-borderd table-hover'>
      <thead>
        <tr>
          <th>Price</th>
          <th>Category</th>
          <th>Description</th>
          <th>Income ?</th>
          <th>Date</th>
        </tr>
      </thead>
      <tbody>
        {transactions.map((transaction) => (
          <tr key={transaction.id}>
            <td>{transaction.price}</td>
            <td>{transaction.category}</td>
            <td>{transaction.description}</td>
            <td>{transaction.is_income ? 'Yes' : 'No'}</td>
            <td>{transaction.date}</td>
            <td>
              <button type="btn" className="btn btn-primary" onClick={() => handleEditClick(transaction.id)}>
                Edit
              </button>
            </td>
            <td>
              <button type='btn' className='btn btn-danger' onClick={() => handleDeleteClick(transaction.id)}>
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
    {balanceData && ( 
                <div>
                    <h3>Total Income: {balanceData.total_income}</h3>
                    <h3>Total Expenses: {balanceData.total_expenses}</h3>
                    <h3>Balance: {balanceData.balance}</h3>
                </div>
                )}
      <br />
      <Charts expenseData={chartData.expense_data} incomeData={chartData.income_data} />
    </div>
    );
};


export default Home;
