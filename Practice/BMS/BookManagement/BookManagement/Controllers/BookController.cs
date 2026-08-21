using BookManagement.DTOs;
using BookManagement.Services;
using Microsoft.AspNetCore.Mvc;

namespace BookManagement.Controllers
{
    public class BookController : Controller
    {
        private readonly IBookService _bookService;

        public BookController(IBookService bookService)
        {
            _bookService = bookService;
        }

        public IActionResult Dashboard()
        {
            var books = _bookService.GetAll();
            return View(books);
        }

        [HttpGet]
        public IActionResult Create()
        {
            return View();
        }
    }
}
