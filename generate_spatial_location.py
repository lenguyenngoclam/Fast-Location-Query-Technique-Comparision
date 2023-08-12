import numpy as np
import decimal
import random
import argparse


class Coordinate:
    def __init__(self, longitude, latitude, name: str = "NULL"):
        self.longitude = longitude
        self.latitude = latitude
        self.name = name

    def __str__(self):
        return f"({self.name}, {self.longitude}, {self.latitude})"

    def get_point_format(self):
        """
        Return string that convert longitude and latitude to POINT type in MySQL database
        """

        return f"({self.name}, ST_GeomFromText('POINT({self.latitude} {self.longitude})', 4326))"


def generate_spatial_location(num_samples: int = int(1e6)):
    coordinates = []

    for _ in range(num_samples):
        lon = decimal.Context(prec=9).create_decimal_from_float(random.uniform(-180, 180))
        lat = decimal.Context(prec=8).create_decimal_from_float(random.uniform(-90, 90))
        coordinates.append(Coordinate(longitude=lon, latitude=lat))

    return coordinates


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simple program for generating geography coordinate"
    )

    parser.add_argument(
        "-ns",
        "--num-samples",
        help="Number of coordinates to generate",
        required=True,
        type=int,
        default=100,
    )

    args = vars(parser.parse_args())

    coordinates = generate_spatial_location(args["num_samples"])
