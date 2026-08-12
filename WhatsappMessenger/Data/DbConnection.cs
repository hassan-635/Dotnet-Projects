using Microsoft.Data.SqlClient;
namespace WhatsappMessenger.Data;

public class DbConnection
{
    private readonly IConfiguration _configuration;
    public DbConnection(IConfiguration configuration)
    {
        _configuration = configuration;
    }

    public SqlConnection CreateConnection()
    {
        var connectionString = _configuration.GetConnectionString("DefaultConnection");
        return new SqlConnection(connectionString);
    }
}