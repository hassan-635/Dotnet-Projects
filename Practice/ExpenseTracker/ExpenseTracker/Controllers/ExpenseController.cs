using ExpenseTracker.DTOs;
using ExpenseTracker.Services;
using Microsoft.AspNetCore.Mvc;

namespace ExpenseTracker.Controllers
{
    public class ExpenseController : Controller
    {
        private readonly IExpenseService _expenseService;

        public ExpenseController(IExpenseService expenseService)
        {
            _expenseService = expenseService;
        }

        [HttpGet]
        public IActionResult Dashboard()
        {
            var expenses = _expenseService.GetAllExpenses();
            return View(expenses);
        }

        [HttpGet]
        public IActionResult AddExpense()
        {
            return View();
        }

        [HttpPost]
        public IActionResult AddExpense(ExpenseDTO Expense)
        {
            if(!ModelState.IsValid)
                return View(Expense);

            _expenseService.AddExpense(Expense);
            return RedirectToAction("Dashboard");
        }

        [HttpGet]
        public IActionResult GetById()
        {
            return View();
        }

        [HttpPost]
        public IActionResult GetById(int id)
        {
            var expense = _expenseService.GetExpenseById(id);
            return View("GetByIdResult", expense);
        }

        [HttpGet]
        public IActionResult UpdateExpense()
        {
            return View();
        }

        [HttpPost]
        public IActionResult UpdateExpense(int Id)
        {
            var expense = _expenseService.GetExpenseById(Id);
            if(expense == null)
                return NotFound();
            return View("UpdateForm", expense);
        }
        [HttpPost]
        public IActionResult UpdateForm(ExpenseDTO Expense)
        {
            if(!ModelState.IsValid)
                return View(Expense);

            _expenseService.UpdateExpense(Expense);
            return RedirectToAction("Dashboard");
        }

        [HttpGet]
        public IActionResult Delete()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Delete(int id)
        {
            var expense = _expenseService.GetExpenseById(id);
            if (expense == null)
                throw new Exception("Expense Not Found");
            _expenseService.DeleteExpense(id);
            return RedirectToAction("Dashboard");
        }
    }
}
