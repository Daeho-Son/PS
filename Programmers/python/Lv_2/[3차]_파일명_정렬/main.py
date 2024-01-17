from run_test import run_test
from solution import solution


def main():
    test_case = [
        [["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"], ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]],
        [["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"], ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]],
        [["IMG02.png", "IMG01.png", "img02.png", "img01.png"], ["IMG01.png", "img01.png", "IMG02.png", "img02.png"]],
        [["img02.png", "img01.png", "IMG02.png", "IMG01.png"], ["img01.png", "IMG01.png", "img02.png", "IMG02.png"]],
        [["img02.png", "img0001.png", "IMG00002.png", "IMG01.png"], ["img0001.png", "IMG01.png", "img02.png", "IMG00002.png"]],
        [[], []],
        [["_02.png", "_01.png"], ["_01.png", "_02.png"]],
        [[" 02.png", " 01.png"], [" 01.png", " 02.png"]],
        [[" 02", " 01"], [" 01", " 02"]],
        [[" 02 ", " 01 "], [" 01 ", " 02 "]],
        [["02 ", "01 "], ["01 ", "02 "]],
        [["02.01png", "01.01png"], ["01.01png", "02.01png"]]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
