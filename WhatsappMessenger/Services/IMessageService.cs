using WhatsappMessenger.DTOs;
using WhatsappMessenger.Models;
using WhatsappMessenger.Repositories;

namespace WhatsappMessenger.Services;

public interface IMessageService
{
    Task<int> SaveMessageAsync(sendMessageDto dto);
}

public class MessageService : IMessageService
{
    private readonly IMessageRepository _messageRepository;
    public MessageService(IMessageRepository messageRepository)
    {
        _messageRepository = messageRepository;
    }

    public async Task<int> SaveMessageAsync(sendMessageDto dto)
    {
        byte[]? fileData = null;
        if(dto.Pdf != null)
        {
            using var memoryStream = new MemoryStream();
            await dto.Pdf.CopyToAsync(memoryStream);
            fileData = memoryStream.ToArray();
        }

        var message = new Message
        {
            phoneNumber = dto.PhoneNumber,
            MessageText = dto.MessageText,
            FileName = dto.Pdf?.FileName,
            FileData = fileData
        };

        return await _messageRepository.SaveMessageAsync(message);
    }
}