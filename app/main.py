class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step  # + Y

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step  # - Y

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step  # + X

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step  # - X

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step  # + Z

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step  # - Z


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        max_load_weight: int,
        current_load: Cargo = None,
        coords: list = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
