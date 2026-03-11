from enum import Enum


class PipelineType(Enum):
    BULLETING = "bulletin"
    BIDDING = "bidding"
    COMPARE = "compare"


class PeriodType(Enum):
    MRN = "MRN"
    AFT = "AFT"
    EVN = "EVN"


class WorkerStatus(Enum):
    success = "success"
    progress = "progress"
    failure = "failure"
