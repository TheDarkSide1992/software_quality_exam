import datetime
import uuid
from uuid import UUID, uuid4
from datetime import datetime
from dataclasses import dataclass, field

@dataclass()
class Booking:
    id: UUID
    StartDate: datetime
    EndDate: datetime
    CustomerId: UUID
    RoomId: UUID


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