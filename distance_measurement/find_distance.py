import math
from collections import namedtuple

Point = namedtuple("Point", "longitude latitude")


def point_to_radian(point: tuple[float, float]) -> Point:
    return Point(math.radians(point[0]), math.radians(point[1]))


def find_the_distance(point1: Point, point2: Point) -> float:
    earth_radius = 6371  # in km
    central_angle1 = 2 * math.asin(math.sqrt(
        math.sin((point2.longitude - point1.longitude) / 2) ** 2 +
        math.cos(point1.longitude) * math.cos(point2.longitude) *
        math.sin((point2.latitude - point1.latitude) / 2) ** 2))

    distance = earth_radius * central_angle1

    return distance
