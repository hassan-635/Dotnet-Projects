using BookManagement.DTOs;

namespace BookManagement.Services
{
    public class BookService
    {
        private static List<BookDto> books = new List<BookDto>();
        public List<BookDto> GetAll()
        {
            return books;
        }

        public BookDto? GetById(int Id)
        {
            return books.FirstOrDefault(book => book.Id == Id);
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
