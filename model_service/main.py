import uvicorn


def main():

    uvicorn.run(
        app="wsgi:app",
        port=5040,
        log_level="info",
        reload=True,
    )


if __name__ == "__main__":
    main()
