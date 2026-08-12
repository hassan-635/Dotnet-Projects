# WhatsApp Messenger API

A simple ASP.NET Core Web API to send WhatsApp messages with optional PDF attachments, backed by SQL Server via Dapper.

---

## Tech Stack

- **Backend** — ASP.NET Core (.NET 10)
- **Database** — SQL Server + Dapper
- **Frontend** — HTML / CSS / Vanilla JS (served from `wwwroot`)
- **Docs** — Swagger / OpenAPI

---

## Project Structure

```
WhatsappMessenger/
├── Controllers/        # API endpoints
├── Services/           # Business logic
├── Repositories/       # Database queries (Dapper)
├── Models/             # Domain models
├── DTOs/               # Request/response shapes
├── Data/               # DB connection helper
└── wwwroot/            # Static frontend (index.html)
```

---

## API Endpoint

### `POST /api/Messages/Send`

Sends a WhatsApp message and optionally saves a PDF attachment.

**Content-Type:** `multipart/form-data`

| Field | Type | Required |
|---|---|---|
| `PhoneNumber` | string | ✅ |
| `MessageText` | string | ✅ |
| `Pdf` | file (.pdf) | ❌ |

**Success Response:**
```json
{
  "success": true,
  "message": "Message Saved Successfully!!!",
  "id": 1
}
```

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/WhatsappMessenger.git
cd WhatsappMessenger
```

### 2. Set up the database

Create the `Messages` table in SQL Server:

```sql
CREATE TABLE Messages (
    Id          INT IDENTITY(1,1) PRIMARY KEY,
    PhoneNumber NVARCHAR(20)  NOT NULL,
    MessageText NVARCHAR(MAX) NULL,
    FileName    NVARCHAR(255) NULL,
    FileData    VARBINARY(MAX) NULL,
    CreatedAt   DATETIME DEFAULT GETDATE()
);
```

### 3. Update connection string

In `appsettings.json`:
```json
"ConnectionStrings": {
  "DefaultConnection": "Server=YOUR_SERVER;Database=YOUR_DB;Trusted_Connection=True;"
}
```

### 4. Run
```bash
dotnet run
```

App opens at `https://localhost:{port}` — frontend loads automatically.  
Swagger UI available at `https://localhost:{port}/swagger`.

---

## Deployment

| What | Where |
|---|---|
| Backend + Frontend | Azure App Service |
| Database | Azure SQL Database |

> **Tip:** Azure is recommended since it natively supports .NET and SQL Server — no code changes needed.

---

## License

MIT
