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

"""
 public class Booking
    {
        public int Id { get; set; }
        public DateTime StartDate { get; set; }
        public DateTime EndDate { get; set; }
        public bool IsActive { get; set; }
        public int CustomerId { get; set; }
        public int RoomId { get; set; }
        public virtual Customer Customer { get; set; }
        public virtual Room Room { get; set; }
    }
"""