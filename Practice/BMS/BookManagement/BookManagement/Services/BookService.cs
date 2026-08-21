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

        public void Add(BookDto book)
        {
            book.Id = books.Count + 1;
            books.Add(book);
        }

        public void Update(BookDto book)
        {

        }

        public void Delete(int id)
        {

        }
    }
}
