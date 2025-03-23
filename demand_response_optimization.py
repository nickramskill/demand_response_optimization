from pyomo.environ import ConcreteModel, Var, Objective, ConstraintList, NonNegativeReals, SolverFactory, minimize, value, RangeSet
import numpy as np
import matplotlib.pyplot as plt
from utils import read_data

class DemandResponse(): 
    def __init__(self, base_load, min_load, max_load, defer_cost, shed_cost):
        self.price_data = read_data()
        self.hours = list(range(len(self.price_data)))
        self.base_load = np.full(len(self.price_data), base_load)
        self.min_load = min_load
        self.max_load = max_load
        self.defer_cost = defer_cost
        self.shed_cost = shed_cost
        self.model = ConcreteModel()
        self._build_model()

    def _build_model(self):
        self.model.time_axis = RangeSet(0, len(self.price_data) - 1)
        self.model.load_optimized = Var(self.model.time_axis, domain=NonNegativeReals)
        self.model.load_shed = Var(self.model.time_axis, domain=NonNegativeReals)
        self.model.load_defer = Var(self.model.time_axis, domain=NonNegativeReals)

        self.model.constraints = ConstraintList()
        for t in self.model.time_axis:
            defered_in = self.model.load_defer[t - 1] if t > 0 else 0
            self.model.constraints.add(
                self.model.load_optimized[t] == self.base_load[t] - self.model.load_shed[t] - self.model.load_defer[t] + defered_in
            )
            self.model.constraints.add(self.model.load_optimized[t] >= self.min_load)
            self.model.constraints.add(self.model.load_optimized[t] <= self.max_load)

        self.model.constraints.add(
            sum(self.model.load_defer[t] for t in self.model.time_axis) == sum(self.model.load_defer[t-1] for t in self.model.time_axis if t > 0)
        )

        def objective_function(model):
            return sum(
                self.price_data[t] * model.load_optimized[t] +
                self.defer_cost * model.load_defer[t] +
                self.shed_cost * model.load_shed[t]
                for t in model.time_axis
            )
        
        self.model.objective = Objective(rule=objective_function, sense=minimize)

    def _solve_model(self, solver='cbc'):
        solver = SolverFactory(solver)
        solver.solve(self.model)

    def _get_results(self):
        self.load_optimized = [value(self.model.load_optimized[t]) for t in self.model.time_axis]
        self.load_shed = [value(self.model.load_shed[t]) for t in self.model.time_axis]
        self.load_defer = [value(self.model.load_defer[t]) for t in self.model.time_axis]
        self._plot_results()

    def _plot_results(self):
        fig, ax1 = plt.subplots(figsize=(12, 5))
        ax1.plot(self.base_load, label="Baseline Load", linestyle="--")
        ax1.plot(self.load_optimized, label="Optimized Load")
        ax1.bar(self.hours, self.load_shed, label="Shed Load", alpha=0.3)
        ax1.bar(self.hours, self.load_defer, label="Deferred Load", bottom=self.load_shed, alpha=0.3)
        ax1.set_xlabel("Hour")
        ax1.set_ylabel("Optimized Load (MW)")
        ax1.grid(True)
        ax2 = ax1.twinx()
        ax2.plot(self.price_data, label="Price ($/MWh)", color="orange", linestyle="--")
        ax2.set_ylabel("Price ($/MWh)", color="orange")
        ax2.tick_params(axis='y', labelcolor="orange")
        lines_1, labels_1 = ax1.get_legend_handles_labels()
        lines_2, labels_2 = ax2.get_legend_handles_labels()
        ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')
        plt.title("Data Center Demand Response Optimization")
        plt.tight_layout()
        plt.savefig("demand_response_optimization.png", dpi=300)
        plt.show()

if __name__ == "__main__":
    base_load = 10
    min_load = 6
    max_load = 12
    defer_cost = 20
    shed_cost = 50
    model = DemandResponse(base_load, min_load, max_load, defer_cost, shed_cost)
    model._solve_model()
    model._get_results()