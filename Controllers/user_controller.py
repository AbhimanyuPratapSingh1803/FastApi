from fastapi import APIRouter, HTTPException
from Models.user_model import User, UpdateUser
from bson.objectid import ObjectId
from DB.database import get_collection

router = APIRouter()

collection = get_collection("users")

@router.post("/addUser", response_model=dict)
async def add_user(user: User):
    user = collection.insert_one(user.dict())
    if not user:
        raise HTTPException(status_code=400, detail="User not created")
    return {
        "message": "User created successfully",
        "user_id": str(user.inserted_id)
    }

@router.get("/getUser/{user_id}", response_model=dict)
async def get_user(user_id: str):
    try:
        user = collection.find_one({"_id": ObjectId(user_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user ID format")
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["_id"] = str(user["_id"])
    return {
        "message": "User found successfully",
        "user": user
    }

@router.get("/getAllUsers", response_model=dict)
async def get_all_users():
    try:
        users = collection.find()
    except Exception:
        raise HTTPException(status_code=400, detail="Could not retrieve users")

    user_list = []
    
    for user in users:
        user["_id"] = str(user["_id"])
        user_list.append(user)
    
    return {
        "message": "Users retrieved successfully",
        "users": user_list
    }

@router.put("/updateUser/{user_id}", response_model=dict)
async def update_user(user_id: str, user: UpdateUser):
    updatedUser = collection.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict()})
    if not updatedUser:
        raise HTTPException(status_code=400, detail="User not updated")
    return {
        "message": "User updated successfully",
        "user": user
    }

@router.delete("/deleteUser/{user_id}", response_model=dict)
async def delete_user(user_id: str):
    user = collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User to be deleted doesn't exist")

    deletedUser = collection.delete_one({"_id": ObjectId(user_id)})
    if not deletedUser:
        raise HTTPException(status_code=400, detail="User not deleted")
    return {
        "message" : "User deleted successfully",
    }