import pytest

from second_task.models.colors import Colors
from second_task.models.engine2d import Engine2D
from second_task.models.shapes.circle import Circle
from second_task.models.shapes.rectangle import Rectangle
from second_task.models.shapes.triangle import Triangle


class TestEngine2D:
    @pytest.mark.parametrize("radius", [1, 100])
    def test_circle_draw_with_correct_radius(self, capsys, radius):
        # arrange
        engine = Engine2D()
        engine.add_shape(Circle(radius))

        # act
        engine.draw()
        captured = capsys.readouterr().out

        assert '*' in captured
        assert f'Drawing Circle with radius={radius}' in captured

    @pytest.mark.parametrize("radius", [0, -1, -100])
    def test_circle_draw_with_invalid_radius(self, capsys, radius):
        # arrange
        engine = Engine2D()
        engine.add_shape(Circle(radius))

        # act
        engine.draw()
        captured = capsys.readouterr().out

        assert not captured
        assert '*' not in captured
        assert f'Drawing Circle with radius={radius}' not in captured

    @pytest.mark.parametrize("height_width", [(1, 1), (100, 100), (1, 100), (100, 1)])
    def test_rectangle_draw_with_correct_parameters(self, capsys, height_width):
        engine = Engine2D()
        height, width = height_width
        engine.add_shape(Rectangle(height, width))
        engine.draw()
        captured = capsys.readouterr().out

        assert '*' in captured
        assert f'Drawing Rectangle with height={height} and width={width}' in captured

    def test_rectangle_draw(self, capsys):
        engine = Engine2D()
        height, width = 2, 2
        expected_output = '''**\n**'''
        engine.add_shape(Rectangle(height, width))
        engine.draw()
        captured = capsys.readouterr().out

        assert f'Drawing Rectangle with height={height} and width={width}' in captured
        assert expected_output in captured

    @pytest.mark.parametrize("height_width", [(0, 0), (0, 1), (1, 0), (1, -1), (1, -1), (-1, -1)])
    def test_rectangle_draw_with_incorrect_parameters(self, capsys, height_width):
        engine = Engine2D()
        height, width = height_width
        engine.add_shape(Rectangle(height, width))
        engine.draw()
        captured = capsys.readouterr().out

        assert '*' not in captured
        assert f'Drawing Rectangle with height={height} and width={width}' not in captured

    @pytest.mark.parametrize("height", [1, 100])
    def test_triangle_draw_info(self, capsys, height):
        engine = Engine2D()
        engine.add_shape(Triangle(height))
        engine.draw()
        captured = capsys.readouterr().out

        assert '*' not in captured
        assert f'Drawing Triangle with height={height}' in captured

    @pytest.mark.parametrize("height", [0, -1])
    def test_triangle_draw_info(self, capsys, height):
        engine = Engine2D()
        engine.add_shape(Triangle(height))
        engine.draw()
        captured = capsys.readouterr().out

        assert not captured
        assert '*' not in captured
        assert f'Drawing Triangle with height={height}' not in captured

    @pytest.mark.parametrize("color", [Colors.GREEN,
                                       Colors.CYAN,
                                       Colors.BLUE,
                                       Colors.RED,
                                       Colors.YELLOW])
    def test_engine_color(self, capsys, color):
        # arrange
        engine = Engine2D()
        engine.add_shape(Rectangle(8, 10))

        # act
        engine.set_color(color)
        engine.draw()
        captured = capsys.readouterr().out

        assert_color_is_in_captured(color, captured)

    def test_change_engine_color(self, capsys):
        # arrange
        engine = Engine2D()
        shape = Triangle(5)
        engine.add_shape(shape)

        first_color = Colors.BLUE
        second_color = Colors.GREEN

        engine.set_color(first_color)
        engine.draw()
        captured_before_change = capsys.readouterr().out

        # act
        engine.set_color(second_color)
        engine.add_shape(shape)
        engine.draw()
        captured_after_change = capsys.readouterr().out

        assert_color_is_in_captured(first_color, captured_before_change)
        assert_color_is_not_in_captured(first_color, captured_after_change)
        assert_color_is_in_captured(second_color, captured_after_change)

    def test_color_stays_the_same_for_all_drawings_after_first_draw(self, capsys):
        # arrange
        engine = Engine2D()
        shape = Triangle(5)
        shape2 = Rectangle(5, 15)
        color = Colors.YELLOW

        # act
        engine.set_color(color)
        engine.add_shape(shape)
        engine.draw()

        engine.add_shape(shape2)
        engine.draw()
        captured = capsys.readouterr().out

        assert_color_is_in_captured(color, captured)

    def test_standard_engine_color(self, capsys):
        # arrange
        engine = Engine2D()
        engine.add_shape(Rectangle(1, 1))

        # act
        engine.draw()

        captured = capsys.readouterr().out

        assert f'Current color is ' not in captured

    def test_canvas_cleared_after_drawing(self, capsys):
        # arrange
        engine = Engine2D()
        engine.add_shape(Rectangle(2, 2))

        # act
        engine.draw()
        capsys.readouterr()
        engine.draw()
        captured = capsys.readouterr().out

        assert len(captured) == 0

    def test_draw_empty_canvas(self, capsys):
        # arrange
        engine = Engine2D()

        # act
        engine.draw()
        captured = capsys.readouterr().out

        assert len(captured) == 0


def assert_color_is_in_captured(color, captured):
    assert color.name in captured
    assert color.value in captured
    assert f'Current color is {color.name}. ' in captured


def assert_color_is_not_in_captured(color, captured):
    assert color.name not in captured
    assert color.value not in captured
    assert f'Current color is {color.name}. ' not in captured
