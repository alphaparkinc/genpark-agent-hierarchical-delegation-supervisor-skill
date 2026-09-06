"""
Demonstration of genpark-agent-hierarchical-delegation-supervisor-skill
"""

from client import HierarchicalSupervisorClient

def main():
    supervisor = HierarchicalSupervisorClient()

    # Register worker agents
    supervisor.register_worker("Researcher", lambda q: "Identified 3 top market competitors: A, B, C.")
    supervisor.register_worker("Engineer", lambda q: "Built benchmark scraper script in Python.")

    goal = "Research competitors and build benchmark pipeline code"
    report = supervisor.execute_hierarchy(goal)

    print("=== HIERARCHICAL SWARM EXECUTION REPORT ===")
    print("Goal:", report["goal"])
    print("Subtasks Executed:", report["subtasks_executed"])
    print("
" + report["final_synthesis"])

if __name__ == "__main__":
    main()
