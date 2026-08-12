using Microsoft.AspNetCore.Http;
namespace WhatsappMessenger.DTOs;

public class sendMessageDto
{
    public string PhoneNumber { get; set; } = string.Empty;
    public string MessageText { get; set; } = string.Empty;
    public IFormFile? Pdf { get; set; }
}