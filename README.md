# 🌦 MCP Weather Server with Claude Desktop Integration

## 📌 Overview

This project demonstrates how to build a **Model Context Protocol (MCP) server** using Python and integrate it with Claude Desktop to enable real-time tool execution.

The server provides weather-related tools that fetch **live data from the National Weather Service API (weather.gov)**.

---

## 🧠 What is MCP?

MCP (Model Context Protocol) allows AI models like Claude to:

* Call external tools
* Fetch real-time data
* Execute backend logic

---

## ⚙️ Features

* 🔥 Custom MCP server using FastMCP
* 🌍 Real-time weather alerts
* 🌤 Weather forecast support
* 🔌 Integration with Claude Desktop
* ⚡ Async API calls using httpx

---

## 🧩 Tools Implemented

### 1. `get_alerts(state)`

Fetches active weather alerts for a US state.

Example:

```bash
Get alerts for CA
```

---

### 2. `get_forecast(lat, lon)`

Fetches weather forecast using latitude and longitude.

Example:

```bash
Get forecast for 37.77 -122.41
```

---

### 3. `test_tool()`

Simple tool to verify MCP connection.

---

## 🔄 Architecture

```
User → Claude Desktop
        ↓
     MCP Protocol
        ↓
   Python MCP Server
        ↓
   weather.gov API
        ↓
     Response → Claude → User
```

---

## 🛠️ Tech Stack

* Python
* FastMCP (MCP SDK)
* httpx (async requests)
* Claude Desktop
* uv (package manager)

---

## ⚙️ Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/your-username/MCP-Weather-Server.git
cd MCP-Weather-Server
```

---

### 2. Install Dependencies

```bash
pip install mcp httpx
```

---

### 3. Run Server (Test)

```bash
uv run weather.py
```

---

### 4. Configure Claude Desktop

Add config:

```json
{
  "mcpServers": {
    "weather": {
      "command": "C:\\Python314\\Scripts\\uv.exe",
      "args": [
        "run",
        "--python",
        "C:\\Python314\\python.exe",
        "D:\\learnTASK\\MCPtask\\weather.py"
      ],
      "cwd": "D:\\learnTASK\\MCPtask"
    }
  }
}
```

---

### 5. Restart Claude Desktop

---

## 🧪 Example Output

```
Get alerts for CA

Winter Weather Advisory:
- Snow up to 6 inches
- Winds up to 40 mph
```

---

## ⚠️ Challenges Faced

* Python version mismatch
* Dependency issues (httpx not found)
* MCP server disconnection errors
* Claude not loading config

---

## ✅ Solutions

* Forced Python version using uv
* Installed dependencies globally
* Debugged using logs
* Ensured server runs with stdio transport

---

## 🎯 Key Learnings

* MCP architecture and workflow
* Tool-based AI interaction
* API integration with LLMs
* Debugging real-world systems

---

## 🚀 Future Improvements

* Add UI dashboard
* Convert to .mcpb extension
* Add more tools (news, maps, DB)
* Multi-agent workflows

---

## 💬 Conclusion

This project demonstrates how to extend AI capabilities using MCP by connecting real-time external data sources, making AI responses dynamic and actionable.

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
