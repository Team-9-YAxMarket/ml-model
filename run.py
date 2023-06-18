from fastapi import FastAPI, Request
import uvicorn
import argparse

from src import create_app

app = create_app()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=8000, type=int, dest="port")
    parser.add_argument("--host", default="0.0.0.0", type=str, dest="host")
    args = vars(parser.parse_args())

    uvicorn.run(app, host=args['host'], port=args['port'])
