using BookManagement.DTOs;
using BookManagement.Services;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore.Metadata.Internal;

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

        [HttpPost]
        public IActionResult Create(BookDto book)
        {
            _bookService.Add(book);
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
            var Book = _bookService.GetById(id);

            if(Book == null)
            {
                return View("GetByIdPost", null);
            }
            return View("GetByIdPost", Book);
        }

        [HttpGet]
        public IActionResult Update()
        {
            return View();
        }

        [HttpGet]
        public IActionResult Update(int id)
        {
            var Book = _bookService.GetById(id);
            if(Book == null)
            {
                return NotFound();
            }

            return View(Book);
        }

        [HttpPost]
        public IActionResult Update(BookDto book)
        {
            if(!ModelState.IsValid)
                return View(book);

            var existingBook = _bookService.GetById(book.Id);

            if (existingBook == null)
                return NotFound();

            _bookService.Update(book);
            return RedirectToAction("Dashboard");
        }

    }
}
