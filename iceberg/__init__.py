__version__ = "0.1.2"

from iceberg.core import (
    Drawable,
    DrawableWithChild,
    Bounds,
    Color,
    Colors,
    Renderer,
    PathStyle,
    FontStyle,
    Corner,
    StrokeCap,
    render_svg,
    AnimatableProperty,
    drawable_field,
    dont_animate,
)

from iceberg.primitives import (
    Rectangle,
    Ellipse,
    Line,
    BorderPosition,
    Path,
    CurvedCubicLine,
    PartialPath,
    Transform,
    Padding,
    Compose,
    Grid,
    Blank,
    Align,
    PointAlign,
    Arrange,
    Directions,
    Anchor,
    SimpleText,
    Text,
    SVG,
    SVGPath,
    Tex,
    MathTex,
    Brace,
    Typst,
    MathTypst,
    Blur,
    Opacity,
    Image,
    SmoothPath,
    Point,
    CubicBezier,
    GridOverlay,
)


from iceberg.primitives.plotting import _MATPLOTLIB_INSTALLED

if _MATPLOTLIB_INSTALLED:
    from iceberg.primitives.plotting import MatplotlibFigure


from iceberg.arrows import (
    Arrow,
    ArrowHead,
    ArrowHeadStyle,
    ArrowAlignDirection,
    LabelArrow,
    ArrowPath,
)

from iceberg.animation import tween, EaseType
from iceberg.animation.scene import Playbook, Animated, Scene, Frozen

__all__ = [
    "Drawable",
    "DrawableWithChild",
    "Bounds",
    "Color",
    "Colors",
    "Renderer",
    "PathStyle",
    "FontStyle",
    "Corner",
    "StrokeCap",
    "render_svg",
    "AnimatableProperty",
    "drawable_field",
    "dont_animate",
    "Rectangle",
    "Ellipse",
    "Line",
    "BorderPosition",
    "Path",
    "CurvedCubicLine",
    "PartialPath",
    "Transform",
    "Padding",
    "Compose",
    "Grid",
    "Blank",
    "Align",
    "PointAlign",
    "Arrange",
    "Directions",
    "Anchor",
    "SimpleText",
    "Text",
    "SVG",
    "Tex",
    "MathTex",
    "Typst",
    "MathTypst",
    "Blur",
    "Opacity",
    "Image",
    "SmoothPath",
    "MatplotlibFigure",
    "Arrow",
    "ArrowHead",
    "ArrowHeadStyle",
    "ArrowAlignDirection",
    "LabelArrow",
    "tween",
    "EaseType",
    "Playbook",
    "Animated",
    "Scene",
    "Frozen",
    "ArrowPath",
    "Point",
    "CubicBezier",
    "SVGPath",
    "Brace",
    "GridOverlay",
]

# Expose commonly used classes and enums directly in the iceberg namespace.
TOP_LEFT = Corner.TOP_LEFT
TOP_MIDDLE = Corner.TOP_MIDDLE
TOP_RIGHT = Corner.TOP_RIGHT
MIDDLE_LEFT = Corner.MIDDLE_LEFT
CENTER = Corner.CENTER
MIDDLE_RIGHT = Corner.MIDDLE_RIGHT
BOTTOM_LEFT = Corner.BOTTOM_LEFT
BOTTOM_MIDDLE = Corner.BOTTOM_MIDDLE
BOTTOM_RIGHT = Corner.BOTTOM_RIGHT

LEFT = Directions.LEFT
RIGHT = Directions.RIGHT
UP = Directions.UP
DOWN = Directions.DOWN

VERTICAL = Arrange.Direction.VERTICAL
HORIZONTAL = Arrange.Direction.HORIZONTAL

BLACK = Colors.BLACK
WHITE = Colors.WHITE
RED = Colors.RED
GREEN = Colors.GREEN
BLUE = Colors.BLUE
YELLOW = Colors.YELLOW
CYAN = Colors.CYAN
MAGENTA = Colors.MAGENTA
TRANSPARENT = Colors.TRANSPARENT
