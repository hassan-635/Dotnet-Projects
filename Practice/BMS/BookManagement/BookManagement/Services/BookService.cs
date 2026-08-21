using BookManagement.DTOs;

namespace BookManagement.Services
{
    public class BookService : IBookService
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
            var existingBook = books.FirstOrDefault(b => b.Id == book.Id);

            if(existingBook == null)
            {
                return;
            }

            existingBook.Title = book.Title;
            existingBook.Author = book.Author;
            existingBook.Price = book.Price;
        }

        public void Delete(int id)
        {
            var existingBook = books.FirstOrDefault(b => b.Id == id);

            if(existingBook == null)
            {
                return;
            }

            books.Remove(existingBook);
        }
    }
}
