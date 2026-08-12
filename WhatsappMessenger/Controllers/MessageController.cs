using Microsoft.AspNetCore.Mvc;
using WhatsappMessenger.DTOs;
using WhatsappMessenger.Services;

namespace WhatsappMessenger.Controllers;

[ApiController]
[Route("api/[controller]")]
public class MessagesController : ControllerBase
{
    private readonly IMessageService _messageService;

    public MessagesController(IMessageService messageService)
    {
        _messageService = messageService;
    }

    [HttpPost("Send")]
    [Consumes("multipart/form-data")]
    public async Task<IActionResult> SendMessage([FromForm] sendMessageDto dto)
    {
        if (string.IsNullOrWhiteSpace(dto.PhoneNumber))
        {
            return BadRequest("Phone Number Required!!!");
        }
        if(string.IsNullOrWhiteSpace(dto.MessageText))
        {
            return BadRequest("Message Required!!!");
        }
        if(dto.Pdf != null)
        {
            if(!Path.GetExtension(dto.Pdf.FileName).Equals(".pdf", StringComparison.OrdinalIgnoreCase))
            {
                return BadRequest("Only PDF Files Are Allowed!!!");
            }
        }

        var id = await _messageService.SaveMessageAsync(dto);

        return Ok(new
        {
            success = true,
            message = "Message Saved Successfully!!!",
            id = id
        });
    }
}