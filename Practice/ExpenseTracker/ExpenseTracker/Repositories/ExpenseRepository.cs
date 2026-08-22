using ExpenseTracker.DTOs;

namespace ExpenseTracker.Repositories
{
    public class ExpenseRepository : IExpenseRepository
    {
        private List<ExpenseDTO> expenses = new List<ExpenseDTO>();

        public List<ExpenseDTO> GetAll()
        {
            return expenses;
        }

        public ExpenseDTO GetById(int Id)
        {
            return expenses.FirstOrDefault(expense => expense.Id == Id);
        }

        public bool Add(ExpenseDTO Expense)
        {
            expenses.Add(Expense);
            return true;
        }

        public bool Update(ExpenseDTO Expense)
        {
            var existingExpense = expenses.FirstOrDefault(expense => expense.Id == Expense.Id);
            if (existingExpense == null) return false;

            existingExpense.Title = Expense.Title;
            existingExpense.Amount = Expense.Amount;
            existingExpense.Category = Expense.Category;
            existingExpense.Date = Expense.Date;

            return true;
        }

        public bool Delete(int Id)
        {
            var existingExpense = expenses.FirstOrDefault(expense => expense.Id == Id);

            if(existingExpense == null) return false;

            expenses.Remove(existingExpense);
            return true;
        }
    }
}
