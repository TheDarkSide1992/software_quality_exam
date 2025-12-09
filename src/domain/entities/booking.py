from datetime import datetime
from dataclasses import dataclass

@dataclass()
class Booking:
    id: int
    start_date: datetime
    end_date: datetime
    is_active:bool
    customer_id: int
    room_id: int
