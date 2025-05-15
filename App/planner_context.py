from App.iplanner import IPlanner


class PlannerContext:
    def __init__(self, strategy: IPlanner) -> None:
        self.strategy = strategy

    def __getattr__(self, name):
        return getattr(self.strategy, name)
