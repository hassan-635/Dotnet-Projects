using ExpenseTracker.DTOs;

namespace ExpenseTracker.Repositories
{
    public interface IExpenseRepository
    {
        public List<ExpenseDTO> GetAll();
        public ExpenseDTO GetById(int Id);
        public bool Add(ExpenseDTO Expense);
        public bool Update(ExpenseDTO Expense);
        public bool Delete(int Id);
    }
}
