from fastapi import FastAPI, HTTPException
import logging

logging.basicConfig(filename="user_controller.log", encoding='utf-8', filemode='a', level=logging.INFO)

logger=logging.getLogger(__name__)

app = FastAPI()


@app.get("/users")
def get_users():
    try:
        logger.info("User data retreived")
        return {"users" :['Harry', 'Lilly', 'James']}
    
    except Exception as e:
        logger.error(e)
        print("Error")