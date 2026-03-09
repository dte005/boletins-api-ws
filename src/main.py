# Author: DGT
# Date: 21/02/2026
# Receives the main command with action e params
# Action will determine witch method will be called
# Params will send the params to that method
import logging

from fastapi import FastAPI

from src.environment import env
from src.logging_setup import logging_setup
from src.routes.bidding.routes import router as bidding_router
from src.routes.bulletin.routes import router as bulletin_router

# configure the level logger
level = env("LOG_LEVEL", default="DEBUG")
logging_setup(level)
logger = logging.getLogger("rpa")
app = FastAPI(title="RPA bulletin & bidding")
app.include_router(bulletin_router)
app.include_router(bidding_router)
