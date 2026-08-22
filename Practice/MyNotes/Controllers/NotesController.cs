using Microsoft.AspNetCore.Mvc;

namespace MyNotes.Controllers
{
    public class NotesController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
