from dim_model.orchestrator import Orchestrator


class Main:
    def __init__(self):
        self._orchestrator = Orchestrator()

    def run_pipeline(self):
        self._orchestrator.run()


if __name__ == "__main__":
    Main().run_pipeline()
