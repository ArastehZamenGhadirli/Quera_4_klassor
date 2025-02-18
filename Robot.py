class Robot:
    def __init__(self, n: int, m: int, i: int, j: int):
        """
        Initializes the Robot with grid dimensions and an initial position.

        Parameters:
        n (int): Number of rows in the grid.
        m (int): Number of columns in the grid.
        i (int): Initial row position of the robot.
        j (int): Initial column position of the robot.
        """
        self._n = n
        self._m = m

        if 0 <= i < n and 0 <= j < m:
            self._i = i
            self._j = j
        else:
            raise ValueError("position is outside of the range")

    def get_i(self) -> int:
        """Returns the current row position."""
        return self.__i

    def set_i(self, value) -> None:
        """Sets the current row position and check  if it is in the grid ."""
        if 0 <= value < self._n:
            self._i = value
        else:
            print("wrong number for row position")

    def get_j(self) -> int:
        """Returns the current column position."""
        return self._j

    def set_i(self, value) -> None:
        """Sets the current column position and check  if it is in the grid ."""
        if 0 <= value < self._m:
            self._j = value
        else:
            print("wrong number for column position")

    def update_position(self, di: int, dj: int):
        """
        Updates the robot's position based on the provided increments if within grid boundaries.

        Parameters:
        di (int): Change in the row position.
        dj (int): Change in the column position.
        """
        new_i = self._i + di
        new_j = self._j + dj
        if di <= self._n and dj <= self._m:
            self._i = new_i
            self._j = new_j
        else:
            print("wrong move!!!!")
        print(f"current location of robot is - > {self._i},{self._j}")
    def move_up(self) ->None:
        """Moves the robot up by increasing i."""
        self.update_position(1, 0)

    def move_down(self) ->None:
        """Moves the robot down by decreasing i."""
        self.update_position(-1, 0)

    def move_left(self) ->None:
        """Moves the robot left by decreasing j."""
        self.update_position(0, -1)

    def move_right(self) ->None:
        """Moves the robot right by increasing j."""
        self.update_position(0, 1)
    #def __str__(self) -> str:
    #    """Returns a string that shows of the robot's current position."""
    #    return f"Robot is at ({self._i}, {self._j})"


r = Robot(5, 5, 2, 2)
r.move_up()
r.move_left()
r.move_down()
r.move_right()
r.move_up()
