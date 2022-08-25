from fastapi import FastAPI

app = FastAPI()

courses = {
    1: {
        "title": "Pascal",
        "lessons": 120,
        "hours": 240
    },
    2: {
        "title": "C",
        "lessons": 250,
        "hours": 520
    }
}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True)