using BookManagement.DTOs;

namespace BookManagement.Services
{
    public class BookService
    {
        public List<BookDto> books = new List<BookDto>();
        public List<BookDto> GetAll()
        {
            return books;
        }

        public BookDto? GetById(int Id)
        {
            BookDto book = new BookDto();
            return book;
        }

        public void Add(BookDto dto)
        {

        }

        public void Update(BookDto dto)
        {

        }

        public void Delete(int id)
        {

        }
    }
}
