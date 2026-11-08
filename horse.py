#values here are just for testing purposes, they should be loaded from board later
N = 100 #length of the board until last part
F = N + 6 #length until end ?

class Horse:
    """
    Represents a horse in the Ludo game. Idea is to be able from game get all possible moves, 
    as well as move the horse and check if it is done.

    Note that, if not specified in the constructor, position is relative to 0,  
    decided by what team it belongs to.
    """
    def __init__(self, team = int, start_pos = 0, N = 51, F = 57) -> None:
        self.pos = start_pos
        self.N = N
        self.F = F
        self.done = False
        self.team = team

    def possible_move_after_roll(self, n = int) -> int:
        """
        Returns what move is possible for the horse given the dice roll n, 
        if return 0, then the horse cannot move
        """
        if self.done:
            return 0
        if self.pos == 0 and n == 6:
            return 1
        else: 
            if self.pos + n <= F:
                return n
        return 0

    def possible_moves_before_roll(self):
        """
        Returns a list of possible rolls and corresponding moves for the horse to move
         after the dice roll, if return None, then the horse cannot move
        """
        rolls_and_moves = []
        if self.done:
            pass
        if self.pos == 0:
            rolls_and_moves.append((6, 1))
        else:
            for i in range(1, 7):
                if self.pos + i <= self.F:
                    rolls_and_moves.append((i, i)) 
        return rolls_and_moves

    def possible_position_after_roll(self, n = int) -> int:
        """
        Returns what position the horse will be in after the dice roll n,
        returns current position if the horse cannot move
        """
        return self.pos + self.possible_move_after_roll(n)

    def possible_positions_before_roll(self) -> list:
        """
        Returns a list of possible rolls and corresponding positions for the horse to move
         after the dice roll, if return None, then the horse cannot move
        """
        rolls_and_positions = []
        if self.done:
            pass
        if self.pos == 0:
            rolls_and_positions.append((6, 1))
        else:
            for i in range(1, 7):
                if self.pos + i <= self.F:
                    rolls_and_positions.append((i, self.pos + i)) 
        return rolls_and_positions

    def move(self, move = int) -> int:
        """
        Only used for valid moves
        """
        self.pos += move

        #update done status
        self.is_done()

        return self.pos

    def is_done(self):
        """
        Returns True if the horse is done (have reached the end)
        """
        self.done = self.pos == F
        return self.done