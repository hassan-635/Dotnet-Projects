using WhatsappMessenger.Models;
namespace WhatsappMessenger.Repositories;

public interface IMessageRepository
{
    Task<int> SaveMessageAsync(Message message);
}