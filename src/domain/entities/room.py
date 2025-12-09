from dataclasses import dataclass

@dataclass()
class Room:
    id: int
    name: str

"""
public class Room
{
    public int Id { get; set; }
    public string Description { get; set; }
}
"""