using WhatsappMessenger.Models;
namespace WhatsappMessenger.Repositories;

public interface ImessageRepository
{
    Task<int> SaveMessageAsync(Message message);
}