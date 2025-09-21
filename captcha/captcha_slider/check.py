import cv2
from new import PuzleSolver

if __name__ == "__main__":
    piece_path = "/Users/baole/Desktop/bao_work/code/captcha/captcha_slider/piece4.png"
    background_path = "/Users/baole/Desktop/bao_work/code/captcha/captcha_slider/background4.png"

    solver = PuzleSolver(piece_path, background_path)

    solution = solver.get_position()
    background = cv2.imread(solver.background_path)
    template, x_inf, y_sup, y_inf = solver._PuzleSolver__piece_preprocessing()
    h, w = template.shape[:2]

    top_left_x = solution + x_inf
    top_left_y = y_sup
    bottom_right_x = top_left_x + w
    bottom_right_y = y_inf

    cv2.rectangle(background, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 3)

    cv2.imshow("Detected Position", background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
