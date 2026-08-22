using ExpenseTracker.DTOs;
using ExpenseTracker.Repositories;

namespace ExpenseTracker.Services
{
    public class ExpenseService : IExpenseService
    {
        private readonly IExpenseRepository _expenseRepository;
        public ExpenseService(IExpenseRepository expenseRepository)
        {
            _expenseRepository = expenseRepository;
        }

        public List<ExpenseDTO> GetAllExpenses()
        {
            return _expenseRepository.GetAll();
        }

        public ExpenseDTO? GetExpenseById(int Id)
        {
            return _expenseRepository.GetById(Id);
        }

        public bool AddExpense(ExpenseDTO Expense)
        {
            if(Expense.Amount <= 0)
            {
                throw new Exception("Amount must be greater than zero");
            }

            return _expenseRepository.Add(Expense);
        }

        public bool UpdateExpense(ExpenseDTO Expense)
        {
            if(Expense.Amount <= 0)
            {
                throw new Exception("Amount must be Greater than zero");
            }
            
            var existingExpense = _expenseRepository.GetById(Expense.Id);
            
            if(existingExpense == null)
            {
                throw new Exception("Expense NotFound!!!");
            }

            return _expenseRepository.Update(Expense);
        }

        public bool DeleteExpense(int Id)
        {
            var existingExpense = _expenseRepository.GetById(Id);

            if(existingExpense == null)
            {
                throw new Exception("Expense NotFound!!!");
            }
            return _expenseRepository.Delete(Id);
        }

        public decimal CalculateTotal()
        {
            var expenses = _expenseRepository.GetAll();
            return expenses.Sum(expense => expense.Amount);
        }

        public decimal GetCategoryTotal(string Category)
        {
            var expenses = _expenseRepository.GetAll();
            return expenses.Where(expense => expense.Category == Category).Sum(expense => expense.Amount);
        }
    }
}
