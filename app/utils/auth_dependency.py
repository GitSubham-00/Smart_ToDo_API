from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.database import db
from app.utils.password_hash import verify_password
from app.utils.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

users_collection = db["users"]


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_collection.find_one({"email": form_data.username})

    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": user["email"]}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
