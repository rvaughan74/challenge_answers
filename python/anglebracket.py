"""#hired.com coding assessment challenge.
For a given string of angle brackets ensure all < and > are matched off.
example
solution("><<>") -> "<><<>>"
--------------------------------
Ryan Vaughan - 2021-09-21
Reason for saving to github repository: Problem stuck in my mind after a
strange error, and then timeout prevented me from solving properly on
hired.com. (Be very careful with recursion...)
"""
from random import choice, randint


def solver(to_solve="", check="<", opposite=">"):
    """solver - return an array of opposite to close off each check in to_solve.

    Args:
            to_solve (str, optional): String to close off each case of check
                            found in. Defaults to "".
            check (str, optional): The opening character. Defaults to "<".
            opposite (str, optional): The closing character. Defaults to ">".

    Returns:
            list[str]: The list of opposites for each check.
    """

    result = list()

    for letter in to_solve:
        if letter in check:
            result.append(opposite)
        elif letter in opposite:
            if len(result) > 0:
                result.pop()

    return result


def solution(st):
    """solution - provide the solution to the assigned problem

    Args:
            st (str): String to solve the problem on.

    Returns:
            str: The solution.
    """

    closing_queue = solver(st, "<", ">")
    opening_queue = solver(st[::-1], ">", "<")

    return "".join(opening_queue) + st + "".join(closing_queue)


if __name__ == "__main__":
    selection = "<>"
    characters = [choice(selection) for i in range(randint(1, 15))]
    test = "".join(characters)
    # test = "><<>"
    print(test)
    print(solution(test))
