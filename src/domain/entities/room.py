from dataclasses import dataclass
from uuid import UUID
from xml.dom.minidom import Entity

@dataclass()
class Room:
    id: UUID
    name: str

"""
public class Room
{
    public int Id { get; set; }
    public string Description { get; set; }
}
"""