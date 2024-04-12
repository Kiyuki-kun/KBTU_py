import pygame
import math

SQUARE = 'SQUARE'
CIRCLE = 'CIRCLE'
TRIANGLE = 'TRIANGLE'
RIGHT_TRIANGLE = 'RIGHT_TRIANGLE'
EQUILATERAL_TRIANGLE = 'EQUILATERAL_TRIANGLE'
RHOMBUS = 'RHOMBUS'

# Screen dimensions
DIS_WIDTH = 640
DIS_HEIGHT = 480
MAIN_SCREEN_SIZE = (DIS_WIDTH, DIS_HEIGHT)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Icon dimensions and positions
ICON_TOP_BAR_HEIGHT = 50
ICON_TOP_BAR_WIDTH = 50
ICON_RECTANGLE_START_X = 0
ICON_RECTANGLE_END_X = 50
ICON_CIRCLE_START_X = 50
ICON_CIRCLE_END_X = 100
ICON_ERASER_START_X = 100
ICON_ERASER_END_X = 150
ICON_RIGHT_TRIANGLE_START_X = 150
ICON_RIGHT_TRIANGLE_END_X = 200
ICON_EQUILATERAL_TRIANGLE_START_X = 200
ICON_EQUILATERAL_TRIANGLE_END_X = 250
ICON_RHOMBUS_START_X = 250
ICON_RHOMBUS_END_X = 300
ICON_RED_COLOR_START_Y = 50
ICON_RED_COLOR_END_Y = 100
ICON_GREEN_COLOR_START_Y = 100
ICON_GREEN_COLOR_END_Y = 150
ICON_BLUE_COLOR_START_Y = 150
ICON_BLUE_COLOR_END_Y = 200
ICON_COLOR_SHAPE_WIDTH = 40
ICON_COLOR_SHAPE_HEIGHT = 30

# Tab colors
TOP_TAB_COLOR = (100, 100, 100)
RIGHT_TAB_COLOR = (80, 80, 80)

# Initialize pygame
pygame.init()


def draw_all_shapes(screen, elements_to_draw):
    for element in elements_to_draw:
        if element['shape'] == SQUARE:
            pygame.draw.rect(screen, element['color'], element['rect'])
        elif element['shape'] == CIRCLE:
            pygame.draw.circle(screen, element['color'], (element['x'], element['y']), element['radius'])
        elif element['shape'] == RIGHT_TRIANGLE or element['shape'] == EQUILATERAL_TRIANGLE or element['shape'] == RHOMBUS:
            pygame.draw.polygon(screen, element['color'], element['points'])


def add_element_rectangle(elements_to_draw, x, y, color):
    rect = pygame.Rect(x - 25, y - 25, 50, 50)
    elements_to_draw.append({'shape': SQUARE, 'rect': rect, 'color': color})


def add_element_circle(elements_to_draw, x, y, color, radius):
    elements_to_draw.append({'shape': CIRCLE, 'x': x, 'y': y, 'color': color, 'radius': radius})


def add_element_right_triangle(elements_to_draw, x, y, color):
    points = [(x, y), (x + 50, y), (x, y - 50)]
    elements_to_draw.append({'shape': RIGHT_TRIANGLE, 'points': points, 'color': color})


def add_element_equilateral_triangle(elements_to_draw, x, y, color):
    height = 50 * math.sqrt(3) / 2
    points = [(x + 25, y), (x + 75, y), (x + 50, y + height)]
    elements_to_draw.append({'shape': EQUILATERAL_TRIANGLE, 'points': points, 'color': color})


def add_element_rhombus(elements_to_draw, x, y, color):
    points = [(x + 25, y), (x + 50, y + 25), (x + 25, y + 50), (x, y + 25)]
    elements_to_draw.append({'shape': RHOMBUS, 'points': points, 'color': color})


def main():
    screen = pygame.display.set_mode(MAIN_SCREEN_SIZE)
    clock = pygame.time.Clock()

    elements_to_draw = []  # List to hold drawn shapes
    is_rectangle_drawer = False
    is_circle_drawer = False
    is_right_triangle_drawer = False
    is_equilateral_triangle_drawer = False
    is_rhombus_drawer = False
    is_eraser = False
    color = BLACK  # Default drawing color

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if event.button == 1:
                    # Check if the mouse click is on the rectangle icon
                    if ICON_RECTANGLE_START_X <= position[0] <= ICON_RECTANGLE_END_X and position[1] < ICON_TOP_BAR_HEIGHT:
                        is_rectangle_drawer = True
                        is_circle_drawer = False
                        is_right_triangle_drawer = False
                        is_equilateral_triangle_drawer = False
                        is_rhombus_drawer = False
                        is_eraser = False
                    # Check if the mouse click is on the circle icon
                    elif ICON_CIRCLE_START_X <= position[0] <= ICON_CIRCLE_END_X and position[1] < ICON_TOP_BAR_HEIGHT:
                        is_circle_drawer = True
                        is_rectangle_drawer = False
                        is_right_triangle_drawer = False
                        is_equilateral_triangle_drawer = False
                        is_rhombus_drawer = False
                        is_eraser = False
                    # Check if the mouse click is on the right triangle icon
                    elif ICON_RIGHT_TRIANGLE_START_X <= position[0] <= ICON_RIGHT_TRIANGLE_END_X and position[1] < ICON_TOP_BAR_HEIGHT:
                        is_right_triangle_drawer = True
                        is_rectangle_drawer = False
                        is_circle_drawer = False
                        is_equilateral_triangle_drawer = False
                        is_rhombus_drawer = False
                        is_eraser = False
                    # Check if the mouse click is on the equilateral triangle icon
                    elif ICON_EQUILATERAL_TRIANGLE_START_X <= position[0] <= ICON_EQUILATERAL_TRIANGLE_END_X and position[1] < ICON_TOP_BAR_HEIGHT:
                        is_equilateral_triangle_drawer = True
                        is_rectangle_drawer = False
                        is_circle_drawer = False
                        is_right_triangle_drawer = False
                        is_rhombus_drawer = False
                        is_eraser = False
                    # Check if the mouse click is on the rhombus icon
                    elif ICON_RHOMBUS_START_X <= position[0] <= ICON_RHOMBUS_END_X and position[1] < ICON_TOP_BAR_HEIGHT:
                        is_rhombus_drawer = True
                        is_rectangle_drawer = False
                        is_circle_drawer = False
                        is_right_triangle_drawer = False
                        is_equilateral_triangle_drawer = False
                        is_eraser = False
                    # Check if the mouse click is on the eraser icon
                    elif ICON_ERASER_START_X <= position[0] <= ICON_ERASER_END_X and position[1] < ICON_TOP_BAR_HEIGHT:
                        is_eraser = True
                        is_rectangle_drawer = False
                        is_circle_drawer = False
                        is_right_triangle_drawer = False
                        is_equilateral_triangle_drawer = False
                        is_rhombus_drawer = False
                    # Check if the mouse click is on the red color icon
                    elif DIS_WIDTH - 70 <= position[0] < DIS_WIDTH - 70 + ICON_COLOR_SHAPE_WIDTH and \
                            ICON_RED_COLOR_START_Y <= position[1] < ICON_RED_COLOR_END_Y:
                        color = RED
                    # Check if the mouse click is on the green color icon
                    elif DIS_WIDTH - 70 <= position[0] < DIS_WIDTH - 70 + ICON_COLOR_SHAPE_WIDTH and \
                            ICON_GREEN_COLOR_START_Y <= position[1] < ICON_GREEN_COLOR_END_Y:
                        color = GREEN
                    # Check if the mouse click is on the blue color icon
                    elif DIS_WIDTH - 70 <= position[0] < DIS_WIDTH - 70 + ICON_COLOR_SHAPE_WIDTH and \
                            ICON_BLUE_COLOR_START_Y <= position[1] < ICON_BLUE_COLOR_END_Y:
                        color = BLUE
                    # Add eraser functionality
                    elif is_eraser:
                        for element in elements_to_draw[:]:
                            if element['shape'] == SQUARE and element['rect'].collidepoint(position):
                                elements_to_draw.remove(element)
                            elif element['shape'] == CIRCLE and (element['x'] - position[0]) ** 2 + (element['y'] - position[1]) ** 2 <= element['radius'] ** 2:
                                elements_to_draw.remove(element)
                            elif element['shape'] == RIGHT_TRIANGLE:
                                if pygame.Rect(element['points'][0][0], element['points'][0][1], 50, 50).collidepoint(position):
                                    elements_to_draw.remove(element)
                            elif element['shape'] == EQUILATERAL_TRIANGLE:
                                # Calculate the bounding box for the equilateral triangle
                                min_x = min(point[0] for point in element['points'])
                                max_x = max(point[0] for point in element['points'])
                                min_y = min(point[1] for point in element['points'])
                                max_y = max(point[1] for point in element['points'])
                                tri_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
                                if tri_rect.collidepoint(position):
                                    elements_to_draw.remove(element)
                            elif element['shape'] == RHOMBUS:
                                # Create a bounding rectangle around the rhombus shape
                                rhombus_rect = pygame.Rect(min(point[0] for point in element['points']),
                                                          min(point[1] for point in element['points']),
                                                          abs(element['points'][1][0] - element['points'][0][0]),
                                                          abs(element['points'][2][1] - element['points'][1][1]))
                                if rhombus_rect.collidepoint(position):
                                    elements_to_draw.remove(element)

                    # Draw shapes
                    elif is_rectangle_drawer:
                        add_element_rectangle(elements_to_draw, position[0], position[1], color)
                    elif is_circle_drawer:
                        add_element_circle(elements_to_draw, position[0], position[1], color, 20)
                    elif is_right_triangle_drawer:
                        add_element_right_triangle(elements_to_draw, position[0] - 25, position[1] - 25, color)
                    elif is_equilateral_triangle_drawer:
                        add_element_equilateral_triangle(elements_to_draw, position[0] - 25, position[1] - 25, color)
                    elif is_rhombus_drawer:
                        add_element_rhombus(elements_to_draw, position[0] - 25, position[1] - 25, color)

        screen.fill(WHITE)  # Clear the screen
        # Draw all shapes
        draw_all_shapes(screen, elements_to_draw)

        # Draw icons and tabs
        pygame.draw.rect(screen, TOP_TAB_COLOR, (0, 0, DIS_WIDTH, 40))
        pygame.draw.rect(screen, RIGHT_TAB_COLOR, (DIS_WIDTH - 80, 0, 80, DIS_HEIGHT))
        pygame.draw.rect(screen, WHITE, (ICON_RECTANGLE_START_X + 5, 5, 40, 30))
        pygame.draw.rect(screen, WHITE, (ICON_CIRCLE_START_X + 5, 5, 40, 30))
        pygame.draw.rect(screen, WHITE, (ICON_ERASER_START_X + 5, 5, 40, 30))
        pygame.draw.rect(screen, WHITE, (ICON_RIGHT_TRIANGLE_START_X + 5, 5, 40, 30))
        pygame.draw.rect(screen, WHITE, (ICON_EQUILATERAL_TRIANGLE_START_X + 5, 5, 40, 30))
        pygame.draw.rect(screen, WHITE, (ICON_RHOMBUS_START_X + 5, 5, 40, 30))
        pygame.draw.rect(screen, RED, (DIS_WIDTH - 70, ICON_RED_COLOR_START_Y, ICON_COLOR_SHAPE_WIDTH,
                                       ICON_COLOR_SHAPE_HEIGHT))
        pygame.draw.rect(screen, GREEN, (DIS_WIDTH - 70, ICON_GREEN_COLOR_START_Y, ICON_COLOR_SHAPE_WIDTH,
                                         ICON_COLOR_SHAPE_HEIGHT))
        pygame.draw.rect(screen, BLUE, (DIS_WIDTH - 70, ICON_BLUE_COLOR_START_Y, ICON_COLOR_SHAPE_WIDTH,
                                        ICON_COLOR_SHAPE_HEIGHT))

        # Draw rectangle icon on rectangle button
        pygame.draw.rect(screen, BLACK, (ICON_RECTANGLE_START_X + 15, 10, 20, 20))

        # Draw circle icon on circle button
        pygame.draw.circle(screen, BLACK, (ICON_CIRCLE_START_X + 25, 20), 10)

        # Draw right triangle icon
        pygame.draw.polygon(screen, BLACK, [(ICON_RIGHT_TRIANGLE_START_X + 10, 10),
                                            (ICON_RIGHT_TRIANGLE_START_X + 10, 40),
                                            (ICON_RIGHT_TRIANGLE_START_X + 40, 40)])

        # Draw equilateral triangle icon
        pygame.draw.polygon(screen, BLACK, [(ICON_EQUILATERAL_TRIANGLE_START_X + 25, 40),
                                            (ICON_EQUILATERAL_TRIANGLE_START_X + 10, 10),
                                            (ICON_EQUILATERAL_TRIANGLE_START_X + 40, 10)])

        # Draw rhombus icon
        pygame.draw.polygon(screen, BLACK, [(ICON_RHOMBUS_START_X + 25, 10),
                                            (ICON_RHOMBUS_START_X + 10, 25),
                                            (ICON_RHOMBUS_START_X + 25, 40),
                                            (ICON_RHOMBUS_START_X + 40, 25)])

        # Draw X icon on eraser button
        pygame.draw.line(screen, BLACK, (ICON_ERASER_START_X + 10, 10), (ICON_ERASER_START_X + 30, 30), 3)
        pygame.draw.line(screen, BLACK, (ICON_ERASER_START_X + 10, 30), (ICON_ERASER_START_X + 30, 10), 3)

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Cap the frame rate


if __name__ == "__main__":
    main()
