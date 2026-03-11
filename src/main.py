# Author: DGT
# Date: 21/02/2026
# Receives the main command with action e params
# Action will determine witch method will be called
# Params will send the params to that method
import logging

from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from src.environment import env
from src.errors_handlers import BusinessException, ErrorsHandlers
from src.logging_setup import logging_setup
from src.routes import bidding_router, bulletin_router, compare_router

# configure the level logger
level = env("LOG_LEVEL", default="DEBUG")
logging_setup(level)
logger = logging.getLogger("rpa")
app = FastAPI(title="RPA bulletin & bidding")
app.include_router(bulletin_router)
app.include_router(bidding_router)
app.include_router(compare_router)
app.add_exception_handler(HTTPException, ErrorsHandlers.http)
app.add_exception_handler(BusinessException, ErrorsHandlers.business)
app.add_exception_handler(Exception, ErrorsHandlers.generic)
