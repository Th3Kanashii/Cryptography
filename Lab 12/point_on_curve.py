#!/usr/bin/python3
def is_point_on_curve(x: int, y: int, p: int) -> bool:
    """
    Check if the point (x, y) lies on the elliptic curve defined by the equation y^2 = (x^3 + x + 1) % p.

    :param x: x-coordinate of the point
    :param y: y-coordinate of the point
    :param p: prime modulus
    :return: True if the point is on the curve, False otherwise
    """
    return (y**2) % p == (x**3 + x + 1) % p


def find_points_on_curve(p: int) -> list:
    """
    Find all points (x, y) on the elliptic curve defined by the equation y^2 = (x^3 + x + 1) % p.

    :param p: prime modulus
    :return: List of points on the curve
    """
    points = []
    for x in range(p):
        for y in range(p):
            if is_point_on_curve(x, y, p):
                points.append((x, y))
    return points


def main() -> None:
    """
    Main function to demonstrate finding points on an elliptic curve.
    """
    # Set the prime modulus (p), for example, p = 23
    p = 23

    # Find all points on the elliptic curve
    points_on_curve = find_points_on_curve(p)

    # Print the result
    print("Points on the elliptic curve (mod {}):".format(p))
    for point in points_on_curve:
        print(point)


if __name__ == "__main__":
    main()
