import pytest

from second_task.models.colors import Colors
from second_task.models.engine2d import Engine2D
from second_task.models.shapes.circle import Circle
from second_task.models.shapes.rectangle import Rectangle
from second_task.models.shapes.triangle import Triangle


class TestEngine2D:
    def test_circle_draw_info(self, capsys):
        engine = Engine2D()
        engine.add_shape(Circle(5))
        engine.draw()
        captured = capsys.readouterr()

        assert 'Drawing Circle with radius=5' in captured.out

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

        assert color.name in captured
        assert color.value in captured

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

        assert first_color.name in captured_before_change
        assert first_color.value in captured_before_change
        assert first_color.name not in captured_after_change
        assert first_color.value not in captured_after_change
        assert second_color.name in captured_after_change
        assert second_color.value in captured_after_change

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
