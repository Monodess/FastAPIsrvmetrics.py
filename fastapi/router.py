import fastapi
from starlette.requests import Request

book_router = fastapi.APIRouter()
@book_router.post("/postbook")
def bookpost_endp():
    print("hello w!")

#2 http m implement the same logic
#m themselves are independent
@book_router.get("/getbook")
@book_router.post("/getandpostbook")
def bookgetpost_endp():
    print("what is this?")

user_router = fastapi.APIRouter()
@user_router.api_route("/user", methods=["GET", "POST"])
async def usergetpost(request: Request):
    print("users endp")
#import only main router in main
main_router = fastapi.APIRouter()

main_router.include_router(book_router)
main_router.include_router(user_router)

if __name__ == '__main__':
     for r in main_router.routes:
      print(r)


