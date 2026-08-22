using ExpenseTracker.DTOs;

namespace ExpenseTracker.Services
{
    public interface IExpenseService
    {
        public List<ExpenseDTO> GetAllExpenses();
        public ExpenseDTO? GetExpenseById(int Id);
        public bool AddExpense(ExpenseDTO Expense);
        public bool UpdateExpense(ExpenseDTO Expense);
        public bool DeleteExpense(int Id);
        public decimal CalculateTotal();
        public decimal GetCategoryTotal(string category);
    }
}
