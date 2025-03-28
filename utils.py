import database

def convert_nl_to_sql(nl_query: str):
    print("Received NL Query:", nl_query)  # Debugging line
    if "total revenue" in nl_query:
        return "SELECT SUM(revenue) FROM sales WHERE quarter = 'Q1 2024'"
    elif "total users" in nl_query:
        return "SELECT COUNT(*) FROM users"
    else:
        return "Invalid query"
def parse_query(query: str):
    """
    Parses a natural language query and returns a structured breakdown.
    """
    # Mocked breakdown for now (you can improve this later)
    if "revenue" in query.lower():
        return {
            "metric": "SUM(revenue)",
            "time_period": "Q1 2024",
            "table": "sales"
        }
    else:
        return {"error": "Could not determine query components"}


def mock_response(sql_query: str):
    return database.mock_data.get(sql_query, "No data available")

def validate_query(nl_query: str):
    return "total revenue" in nl_query or "total users" in nl_query
