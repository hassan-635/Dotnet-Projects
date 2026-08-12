using Dapper;
using WhatsappMessenger.Data;
using WhatsappMessenger.Models;

namespace WhatsappMessenger.Repositories;

public class MessageRepository : IMessageRepository
{
    private readonly DbConnection _dbConnection;
    
    public MessageRepository(DbConnection dbConnection)
    {
        _dbConnection = dbConnection;
    }

    public async Task<int> SaveMessageAsync(Message message)
    {
        const string sql = """
            INSERT INTO Messages
            (
                PhoneNumber,
                MessageText,
                FileName,
                FileData
            )
            VALUES
            (
                @PhoneNumber,
                @MessageText,
                @FileName, 
                @FileData
            );

            SELECT CAST(SCOPE_IDENTITY() AS INT);
            """;

            using var connection = _dbConnection.CreateConnection();
            var id = await connection.ExecuteScalarAsync<int>(
                sql,
                message
            );

            return id;
    }       

}