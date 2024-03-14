from main import feedback, Peg, game, generate_hidden_code, OK

HIDDEN_CODE = [Peg.RED, Peg.BLUE, Peg.YELLOW, Peg.GREEN]


def test_feedback_empty():
    assert feedback(HIDDEN_CODE, (Peg.WHITE, Peg.WHITE, Peg.WHITE, Peg.WHITE)) == []


def test_feedback_red_red_blue_blue_4():
    assert feedback(
        (Peg.RED, Peg.RED, Peg.BLUE, Peg.BLUE),
        (Peg.BLUE, Peg.BLUE, Peg.BLUE, Peg.YELLOW),
    ) == [Peg.BLACK, Peg.WHITE]


def test_feedback_red_red_blue_blue():
    assert feedback(
        (Peg.RED, Peg.RED, Peg.BLUE, Peg.BLUE), (Peg.RED, Peg.RED, Peg.RED, Peg.BLUE)
    ) == [Peg.BLACK, Peg.BLACK, Peg.BLACK]


def test_feedback_red_red_blue_blue_2():
    assert feedback(
        (Peg.RED, Peg.RED, Peg.BLUE, Peg.BLUE), (Peg.RED, Peg.RED, Peg.BLUE, Peg.RED)
    ) == [Peg.BLACK, Peg.BLACK, Peg.BLACK]


def test_feedback_red_red_blue_blue_3():
    assert feedback(
        (Peg.RED, Peg.RED, Peg.BLUE, Peg.BLUE), (Peg.RED, Peg.BLUE, Peg.BLUE, Peg.BLUE)
    ) == [Peg.BLACK, Peg.BLACK, Peg.BLACK]


def test_feedback_ok():
    assert feedback(HIDDEN_CODE, HIDDEN_CODE) == OK


def test_game_lost():
    assert (
        game(
            lambda: (Peg.RED, Peg.BLUE, Peg.BLUE, Peg.BLUE),
            (Peg.RED, Peg.YELLOW, Peg.BLUE, Peg.BLUE),
        )
        == -1
    )


def test_game_ok():
    assert (
        game(
            lambda: (Peg.RED, Peg.YELLOW, Peg.BLUE, Peg.BLUE),
            (Peg.RED, Peg.YELLOW, Peg.BLUE, Peg.BLUE),
        )
        == 1
    )


def test_generate_hidden_code():
    received = generate_hidden_code()
    assert len(received) == 4
    assert all([isinstance(e, Peg) for e in received]) == True
