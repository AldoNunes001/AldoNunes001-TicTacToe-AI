import pytest
import tictactoe as ttt


class TestTicTacToe:

    def test_initial_state(self):
        EMPTY = None
        expected = [[EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY]]

        assert expected == ttt.initial_state()

    def test_player_empty_board(self):
        EMPTY = None
        empty_board = [[EMPTY, EMPTY, EMPTY],
                       [EMPTY, EMPTY, EMPTY],
                       [EMPTY, EMPTY, EMPTY]]

        assert 'X' == ttt.player(empty_board)

    def test_player_full_board(self):
        full_board = [['O', 'X', 'O'],
                      ['X', 'X', 'O'],
                      ['O', 'O', 'X']]

        assert 'X' == ttt.player(full_board)

    def test_player_O_turn(self):
        EMPTY = None
        O_turn = [[EMPTY, 'X', 'O'],
                  [EMPTY, 'X', 'O'],
                  [EMPTY, EMPTY, 'X']]

        assert 'O' == ttt.player(O_turn)

    def test_player_X_turn(self):
        EMPTY = None
        X_turn = [[EMPTY, 'X', 'O'],
                  [EMPTY, 'X', 'O'],
                  [EMPTY, 'O', 'X']]

        assert 'X' == ttt.player(X_turn)

    def test_actions(self):
        EMPTY = None
        board = [[EMPTY, 'X', 'O'],
                 ['X', EMPTY, 'O'],
                 ['X', 'O', EMPTY]]

        expected = set([(0, 0), (1, 1), (2, 2)])

        assert expected == ttt.actions(board)

    def test_result_not_a_valid_action(self):
        EMPTY = None
        board = [[EMPTY, 'X', 'O'],
                 ['X', EMPTY, 'O'],
                 ['X', 'O', EMPTY]]

        with pytest.raises(Exception):
            ttt.result(board, (0, 1))

    def test_result_valid_action(self):
        EMPTY = None
        board = [[EMPTY, 'X', 'O'],
                 ['X', EMPTY, 'O'],
                 ['X', 'O', EMPTY]]

        expected = [[EMPTY, 'X', 'O'],
                    ['X', EMPTY, 'O'],
                    ['X', 'O', 'X']]

        assert expected == ttt.result(board, (2, 2))

    def test_winner_none(self):
        EMPTY = None
        board1 = [[EMPTY, 'X', 'O'],
                 ['X', EMPTY, 'O'],
                 ['X', 'O', EMPTY]]

        board2 = [['O', 'X', 'O'],
                  ['X', 'X', 'O'],
                  ['X', 'O', 'X']]

        assert None == ttt.winner(board1)
        assert None == ttt.winner(board2)

    def test_winner_X(self):
        EMPTY = None
        board1 = [['X', 'X', 'O'],
                 ['X', EMPTY, 'O'],
                 ['X', 'O', EMPTY]]

        board2 = [['X', 'X', 'X'],
                 ['O', EMPTY, 'O'],
                 ['X', 'O', EMPTY]]

        board3 = [['O', 'X', 'X'],
                  ['O', 'X', 'O'],
                  ['X', 'O', 'X']]

        assert 'X' == ttt.winner(board1)
        assert 'X' == ttt.winner(board2)
        assert 'X' == ttt.winner(board3)

    def test_winner_O(self):
        EMPTY = None
        board1 = [[EMPTY, 'X', 'O'],
                  ['X', 'X', 'O'],
                  ['X', 'O', 'O']]

        board2 = [['X', 'X', EMPTY],
                  ['X', EMPTY, EMPTY],
                  [ 'O', 'O', 'O']]

        board3 = [['O', 'X', 'X'],
                  ['X', 'O', 'X'],
                  [EMPTY, 'O', 'O']]

        assert 'O' == ttt.winner(board1)
        assert 'O' == ttt.winner(board2)
        assert 'O' == ttt.winner(board3)

    def test_terminal_false(self):
        EMPTY = None
        board1 = [[EMPTY, 'X', 'O'],
                  ['X', EMPTY, 'O'],
                  ['X', 'O', EMPTY]]

        board2 = [[EMPTY, EMPTY, EMPTY],
                  [EMPTY, EMPTY, EMPTY],
                  [EMPTY, EMPTY, EMPTY]] 

        assert False == ttt.terminal(board1)
        assert False == ttt.terminal(board2)

    def test_terminal_true(self):
        EMPTY = None
        board1 = [['X', 'X', 'O'],
                  ['X', EMPTY, 'O'],
                  ['X', 'O', EMPTY]] 

        board2 = [['O', 'X', 'X'],
                  ['X', 'O', 'X'],
                  [EMPTY, 'O', 'O']] 

        board3 = [['O', 'X', 'O'],
                  ['X', 'X', 'O'],
                  ['X', 'O', 'X']]

        assert True == ttt.terminal(board1)
        assert True == ttt.terminal(board2)
        assert True == ttt.terminal(board3)

    def test_utility(self):
        EMPTY = None
        board1 = [['X', 'X', 'O'],
                  ['X', EMPTY, 'O'],
                  ['X', 'O', EMPTY]] 

        board2 = [['O', 'X', 'X'],
                  ['X', 'O', 'X'],
                  [EMPTY, 'O', 'O']] 

        board3 = [['O', 'X', 'O'],
                  ['X', 'X', 'O'],
                  ['X', 'O', 'X']]

        assert 1 == ttt.utility(board1)
        assert -1 == ttt.utility(board2)
        assert 0 == ttt.utility(board3)

    def test_minimax(self):
        EMPTY = None
        board1 = [['O', 'X', 'O'],
                  ['X', 'X', 'O'],
                  ['X', 'O', 'X']]

        board2 = [[EMPTY, 'X', 'X'],
                  ['X', 'O', 'X'],
                  [EMPTY, 'O', 'O']] 

        board3 = [['X', EMPTY, EMPTY],
                 ['O', EMPTY, 'O'],
                 ['X', 'O', 'X']]

        board4 = [['X', 'O', EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, 'X']]

        board5 = [['X', EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]


        assert None == ttt.minimax(board1)
        assert (0, 0) == ttt.minimax(board2)
        assert (1, 1) == ttt.minimax(board3)
        assert (1, 1) == ttt.minimax(board4)
        assert (1, 1) == ttt.minimax(board5)

