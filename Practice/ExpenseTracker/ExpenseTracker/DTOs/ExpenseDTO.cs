namespace ExpenseTracker.DTOs
{
    public class ExpenseDTO
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public int Amount { get; set; }
        public string Category { get; set; }
        public DateOnly Date { get; set; }
    }
}
