// Charts.jsx
import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import './charts.css';

ChartJS.register(ArcElement, Tooltip, Legend);

const generateRandomColors = (count) => {
  const colors = [];
  for (let i = 0; i < count; i++) {
    const randomColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
    colors.push(randomColor);
  }
  return colors;
};

const Charts = ({ expenseData, incomeData }) => {
  const expenseColors = generateRandomColors(Object.keys(expenseData).length);
  const incomeColors = generateRandomColors(Object.keys(incomeData).length);

  const expenseChartData = {
    labels: Object.keys(expenseData),
    datasets: [
      {
        data: Object.values(expenseData),
        backgroundColor: expenseColors,
      },
    ],
  };

  const incomeChartData = {
    labels: Object.keys(incomeData),
    datasets: [
      {
        data: Object.values(incomeData),
        backgroundColor: incomeColors,
      },
    ],
  };

  return (
    <div className="charts-container">
      <div className="chart-item">
        <h2>Expenses by Category</h2>
        <Pie data={expenseChartData} />
      </div>
      <div className="chart-item">
        <h2>Income by Category</h2>
        <Pie data={incomeChartData} />
      </div>
    </div>
  );
};

export default Charts;