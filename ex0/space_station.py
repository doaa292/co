from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data")
    print("=" * 40)

    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 10, 1, 10, 30),
            notes="All systems operational",
        )

        print("\nValid station data:")
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        if station.is_operational:
            print("Status: Operational\n")
        else:
            print("Status: Non-operational\n")

    except ValidationError as error:
        print("Validation error:")
        for err in error.errors():
            print(err["msg"])

    try:
        print("\nTesting Invalid Data")
        print("=" * 40)

        SpaceStation(
            station_id="IS002",
            name="ISS",
            crew_size=25,
            power_level=85.5,
            oxygen_level=98.2,
            last_maintenance=datetime(2026, 10, 1, 10, 30),
        )

    except ValidationError as error:
        print("\nValidation errors detected:")
        for err in error.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
