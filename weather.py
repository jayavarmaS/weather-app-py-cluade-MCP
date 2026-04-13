from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import sys

# Initialize MCP server
mcp = FastMCP("weather")

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"


# -------------------------------
# Helper function
# -------------------------------
async def make_request(url: str) -> dict[str, Any] | None:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }

    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(url, headers=headers, timeout=30.0)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return None


# -------------------------------
# TOOL 1: Get Alerts
# -------------------------------
@mcp.tool()
async def get_alerts(state: str) -> str:
    """
    Get weather alerts for a US state.

    Args:
        state: Two-letter state code (e.g., CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_request(url)

    if not data or "features" not in data:
        return "❌ Unable to fetch alerts."

    if not data["features"]:
        return f"✅ No active alerts for {state}"

    alerts = []

    for feature in data["features"][:3]:  # limit output
        props = feature["properties"]
        alert = f"""
🚨 Event: {props.get("event", "Unknown")}
📍 Area: {props.get("areaDesc", "Unknown")}
⚠️ Severity: {props.get("severity", "Unknown")}
📝 Description: {props.get("description", "No description")}
"""
        alerts.append(alert)

    return "\n---\n".join(alerts)


# -------------------------------
# TOOL 2: Get Forecast
# -------------------------------
@mcp.tool()
async def get_forecast(lat: float, lon: float) -> str:
    """
    Get weather forecast using latitude & longitude.

    Args:
        lat: Latitude
        lon: Longitude
    """
    # Step 1: Get forecast endpoint
    points_url = f"{NWS_API_BASE}/points/{lat},{lon}"
    points_data = await make_request(points_url)

    if not points_data:
        return "❌ Unable to fetch location data."

    forecast_url = points_data["properties"]["forecast"]

    # Step 2: Get forecast data
    forecast_data = await make_request(forecast_url)

    if not forecast_data:
        return "❌ Unable to fetch forecast."

    periods = forecast_data["properties"]["periods"]

    forecasts = []

    for period in periods[:5]:
        f = f"""
📅 {period["name"]}
🌡 Temp: {period["temperature"]}°{period["temperatureUnit"]}
💨 Wind: {period["windSpeed"]} {period["windDirection"]}
☁️ {period["detailedForecast"]}
"""
        forecasts.append(f)

    return "\n---\n".join(forecasts)


# -------------------------------
# DEBUG TOOL (IMPORTANT)
# -------------------------------
@mcp.tool()
async def test_tool() -> str:
    return "🔥 MCP SERVER WORKING PERFECTLY 🔥"


# -------------------------------
# Run Server
# -------------------------------
def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()