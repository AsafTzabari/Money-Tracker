import React from 'react';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';

const AddNewTransaction = ({ formData, setFormData, transactions, setTransactions ,fetchTransactions}) => {
    const navigate = useNavigate();

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

    const handleInputChange = (event) => {
        const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
        setFormData({
          ...formData,
          [event.target.name]: value
        });
      };

    const handleFormSubmit = async (event) => {
    event.preventDefault();
    try {
      await api.post('/create/', formData);
      fetchTransactions();
      setFormData({
        price: '',
        category: '',
        description: '',
        is_income: false,
        date: ''
      });
      navigate(`/`);
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };

  return (
    <div className='container'>
    <h2>{'Add A New Transaction'}</h2>
      <form onSubmit={handleFormSubmit}>
        <div className='mb-3 mt-3'>
          <label htmlFor='price' className='form-label'>
            Price
          </label>
          <input type='text' className='form-control' id='price' name='price' onChange={handleInputChange} value={formData.price} required 
    pattern="[0-9]+(\.[0-9]+)?"
    title="Please enter a valid number" />
        </div>

        <div className='mb-3'>
        <label htmlFor='is_income' className='form-label'>
        Income ? 
      </label>
      <input type='checkbox' id='is_income' name='is_income' onChange={handleInputChange} checked={formData.is_income} />
      </div>
      <div className='mb-3'>
      <label htmlFor='category' className='form-label'>
      Category
      </label>
      <input type='text' className='form-control' id='category' name='category' onChange={handleInputChange} value={formData.category} required 
    />
        </div>
        <div className='mb-3'>
          <label htmlFor='description' className='form-label'>
            Description
          </label>
          <textarea className='form-control' id='description' name='description' onChange={handleInputChange} value={formData.description} rows={4} />
        </div>
        <div className='mb-3'>
          <label htmlFor='date' className='form-label'>
            Date
          </label>
          <input 
            type='date' 
            className='form-control'
            id='date' 
            name='date' 
            onChange={handleInputChange} 
            value={formData.date} 
          />
        </div>

        <div className='mb-3'>
          <button type='submit' className='btn btn-primary'>
            {'Submit'}
          </button>
        </div>
      </form>
    </div>
  );
}

export default AddNewTransaction;
