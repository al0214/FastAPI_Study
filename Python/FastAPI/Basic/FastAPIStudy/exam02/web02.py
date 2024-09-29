from fastapi import FastAPI, Depends, Query, APIRouter
import uvicorn

app = FastAPI()


def depfunc1():
    pass


def depfunc2():
    pass


router = APIRouter(..., dependencies=[Depends(depfunc1)])

# 의존성 함수:


def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "valid": True}

# 경로 함수 / 웹 엔드포인트


@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

# 의존성 함수:


def check_dep(name: str = Query(...), gender: str = Query(...)):
    if not name:
        raise

# 경로 함수 / 웹 엔드포인트


@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True


if __name__ == "__main__":
    uvicorn.run("127.0.0.1:8080")
