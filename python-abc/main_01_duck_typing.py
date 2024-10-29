#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info
import io
import sys

def test_shape_info():
    """Test shape_info function."""
    circle = Circle(radius=5)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    shape_info(circle)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    print(output)

    assert "Area: 78.5" in output, "Incorrect area output in shape_info"
    assert "Perimeter: 31.4" in output, "Incorrect perimeter output in shape_info"

if __name__ == '__main__':
    test_shape_info()