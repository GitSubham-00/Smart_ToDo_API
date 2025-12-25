from fastapi import APIRouter, HTTPException, status
from app.database import db
from app.schemas.user_schema import UserCreate, UserLogin
from app.models.user import user_model
from app.utils.password_hash import hash_password, verify_password
from app.utils.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

users_collection = db["users"]


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate):
    # Check if user already exists
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(
            status_code=400,
            detail="User with this email already exists"
        )

    hashed_pwd = hash_password(user.password)
    user_data = user_model(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pwd
    )

    users_collection.insert_one(user_data)

    return {"message": "User registered successfully"}


@router.post("/login")
def login(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})

    if not db_user or not verify_password(
        user.password, db_user["hashed_password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        data={"sub": db_user["email"]}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
