using BookManagement.DTOs;

namespace BookManagement.Services
{
    public interface IBookService
    {
        public List<BookDto> GetAll();

        public BookDto? GetById(int id);
        public void Add(BookDto dto);
        public void Update(BookDto dto);
        public void Delete(int id);
    }
}
