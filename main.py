from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import utils, auth  # Importing authentication and utility functions

app = FastAPI()

# Request model for query input
class QueryRequest(BaseModel):
    query: str  # User's natural language query

@app.get("/")
def home():
    return {"message": "Welcome to the Gen AI Analytics Backend!"}

# Query processing endpoint
@app.post("/query")
def query_nl(request: QueryRequest, api_key: str = Depends(auth.validate_api_key)):  
    if not request.query:
        raise HTTPException(status_code=400, detail="Query is required")

    try:
        sql_query = utils.convert_nl_to_sql(request.query)  # Convert query to SQL
        response = utils.mock_response(sql_query)  # Mock response
        return {"query": request.query, "sql": sql_query, "result": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Explain query breakdown
@app.post("/explain")
def explain_query(request: QueryRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query is required")

    try:
        breakdown = utils.parse_query(request.query)  # Parse the query breakdown
        if not breakdown:
            raise HTTPException(status_code=400, detail="Query could not be explained")
        return {"query": request.query, "breakdown": breakdown}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Validate query correctness
@app.post("/validate")
def validate_query(request: QueryRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query is required")

    try:
        is_valid = utils.validate_query(request.query)
        if not is_valid:
            return {"query": request.query, "valid": False, "error": "Query missing a time period or metric"}
        return {"query": request.query, "valid": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
