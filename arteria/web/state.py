class State:
    """
    Status conventions to be returned by arteria services
    when running jobs and querying for their status.
    """
    NONE = "none"
    PENDING = "pending"
    STARTED = "started"
    DONE = "done"
    ERROR = "error"
    CANCELLED = "cancelled"

