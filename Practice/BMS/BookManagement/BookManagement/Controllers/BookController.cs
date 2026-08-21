using Microsoft.AspNetCore.Mvc;

namespace BookManagement.Controllers
{
    public class BookController : Controller
    {
        public IActionResult Dashboard()
        {
            return View();
        }
    }
}
