from enum import Enum


class PeriodType(Enum):
    MRN = "MRN"
    AFT = "AFT"
    EVN = "EVN"


class WorkerStatus(Enum):
    success = "success"
    progress = "progress"
    failure = "failure"
