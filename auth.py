from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

# Define the API key (Should be stored securely in environment variables in production)
API_KEY = "mysecureapikey"

api_key_header = APIKeyHeader(name="X-API-Key")

def validate_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key
