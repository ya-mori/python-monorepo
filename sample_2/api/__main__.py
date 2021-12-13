import uvicorn


if __name__ == '__main__':
    uvicorn.run(
        app="api.app.server:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        workers=1,
    )
