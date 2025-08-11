# db-mcp

A minimal Python MCP (Multi-Component Platform) server for managing and querying a PostgreSQL database. This project uses a repository pattern for database access and exposes endpoints for searching and adding records to a `person` table. Designed for integration with Claude MCP client.
This was mostly a fun side project made in a day not in any way a production ready MCP server, i wanted to see how i could use Copilot or Claude Desktop (or Cursor) like MCP Clients to actually interact and call tools (A simple POSTGRESQL call in this case), this was a fun learning expirience for me :)

<img width="1400" height="920" alt="1_MfI2XLk63rQye0Sh-hAUag" src="https://github.com/user-attachments/assets/09ab4a67-ba7a-481b-b933-1738d4354406" />


---

## Features

- PostgreSQL integration via environment variables
- Repository pattern for clean database logic
- MCP tool endpoints for search and add operations
- Simple configuration and test scripts

---

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL server running
- Claude MCP client (optional)

### Installation

```bash
git clone https://github.com/yourusername/db-mcp.git
cd db-mcp
uv sync
```

### Configuration

Create a `.env` file in the project root:

```
POSTGRES_DATABASE=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Ensure your database has a table named `person` with columns: `id`, `name`, `age`, `gender`.


Ensure to update your MCP Client's JSON to connect to this MCP server (below is an example for claude desktop)

```json
{
  "mcpServers": {
    "db_mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "path\\to\\repo\\db_mcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

---

## Running the Server

```bash
uv run main.py
```

---

## Usage

Endpoints are exposed for:
- Looking up a person by name
- Looking up a person by ID
- Adding a new person

Interact using Claude MCP client or HTTP requests.

---

## Example Screenshots

<img width="547" height="349" alt="image" src="https://github.com/user-attachments/assets/bd9147c0-1cde-4137-a831-6fab40bdec79" />

<img width="1454" height="716" alt="image" src="https://github.com/user-attachments/assets/e48e7a46-a714-4345-b17d-ad637bcc97e1" />

<img width="1133" height="622" alt="image" src="https://github.com/user-attachments/assets/1c6dd0e2-91c9-4f98-b395-9dd544252b46" />

<img width="1228" height="639" alt="image" src="https://github.com/user-attachments/assets/5c5537cd-61e4-467c-85ba-fcd3a5a70d35" />


---

## Project Structure

```
db_mcp/
├── main.py
├── repository.py
├── server.py
├── tools/
│   ├── controller.py
│   └── dbms.py
├── .env
├── test_db.py
├── test_dbms.py
├── test_mcp.py
└── README.md
```

---

## Testing

```bash
python test_db.py
python test_dbms.py
python test_mcp.py
```

---

## License

MIT License

---

## Credits
[MCP Documentation](https://modelcontextprotocol.io/docs/learn/architecture)

Developed by cruelkratos😽 
