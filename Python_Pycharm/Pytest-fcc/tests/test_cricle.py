
import pytest
import source.shapes as shapes
import math

class TestCircle:
    def setup_method(self, method):
         print(f"Setting up {method}")
         self.circle = shapes.Circle(10)

    def teardown_method(self, method):
            print(f"Tearing down {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
        #assert True

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected
