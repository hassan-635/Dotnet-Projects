namespace WhatsappMessenger.Models;

public class Message
{
    public int id { get; set; }
    public string phoneNumber { get; set; } = string.Empty;
    public string? MessageText { get; set; }
    public string? FileName { get; set;}
    public byte[]? FileData { get; set; }
    public DateTime CreatedAt { get; set; }
}