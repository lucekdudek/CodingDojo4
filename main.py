from enum import Enum
import random
from typing import Callable, List, Optional, Tuple, TypeAlias, cast


class Peg(str, Enum):
    WHITE = "W"
    BLACK = "B"
    RED = "r"
    BLUE = "b"
    YELLOW = "y"
    GREEN = "g"

    def __repr__(self) -> str:
        return f"{self.value}: {self.name}"


Code: TypeAlias = Tuple[Peg, Peg, Peg, Peg]

OK = 4 * [Peg.BLACK]


def feedback(hidden_code: Code, guess: Code) -> List[Peg]:
    # TODO optimization consideration: use counter and then 
    hidden_copy: List[Optional[Peg]] = [*hidden_code]
    guess_copy: List[Optional[Peg]] = [*guess]
    result = []

    for idx, given in enumerate(guess_copy):
        if hidden_copy[idx] == given:
            result.append(Peg.BLACK)
            hidden_copy[idx] = None
            guess_copy[idx] = None

    for idx, given in enumerate(guess_copy):
        if given is not None and given in hidden_copy:
            result.append(Peg.WHITE)
            hidden_copy[hidden_copy.index(given)] = None
    return result


def generate_hidden_code() -> Code:
    return cast(Code, tuple(random.choices([e for e in Peg], k=4)))


def get_input() -> Code:
    result: List[Peg] = []
    print(f"Legend: {[peg for peg in Peg]}")

    for count in range(1, 5):
        while True:
            given = input(f"Provide color {count}: ")
            if given == "Esc":
                exit()
            try:
                result.append(Peg(given))
                break
            except ValueError:
                pass
    print(f"Your guess: {result}")
    return cast(Code, tuple(result))


def game(input_func: Callable[[], Code], hidden_code: Code) -> int:
    """Return -1 when the game is lost otherwise return try count on with the game was won."""
    # TODO decouple presentation from logic using events instead of print
    for try_count in range(1, 11):
        print(f"Tries remaining: {11-try_count}")
        feed = feedback(hidden_code, input_func())
        print(f"Feedback: {feed}")
        if feed == 4 * [Peg.BLACK]:
            print("YOUR GUESS WAS RIGHT!!!")
            return try_count
        print(80 * "=")
    print(f"YOU LOST, the right answer is: {[e.name for e in hidden_code]}")
    return -1


if __name__ == "__main__":
    game(get_input, generate_hidden_code())
