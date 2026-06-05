from pydantic import BaseModel

class SpotifyAuthURLResponse(BaseModel):
    auth_url: str

class SpotifyCallBackResponse(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str
    expires_in: int
    
class SpotifyProfileResponse(BaseModel):
    id: str
    email: str | None = None
    display_name: str | None = None
    country: str | None = None
    
@router.post("/signin", response_model=SignInResponse, status_code=HTTP_200_OK)
async def signin(credentials: SignInRequest):
    if not SPOTIFY_CLIENT_ID or not SPOTIFY_REDIRECT_URI:
        raise HTTPException(status_code=500)