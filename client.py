"""
Hierarchical Supervisor-Worker Delegation and Aggregation Swarm.
Zero external dependencies, standard library only.
"""

from typing import Dict, List, Any, Optional, Callable

class HierarchicalSupervisorClient:
    """
    Implements Supervisor-Worker hierarchical delegation pattern:
    - Supervisor partitions complex parent goal into discrete worker sub-tasks
    - Dispatches sub-tasks to specialized domain worker agents
    - Aggregates worker outputs into coherent unified synthesis
    """

    def __init__(self, supervisor_id: str = "supervisor"):
        self.supervisor_id = supervisor_id
        self.workers = {} # worker_role -> callable or descriptor

    def register_worker(self, role: str, worker_fn: Callable[[str], str]):
        """Registers a worker agent capability."""
        self.workers[role] = worker_fn

    def decompose_task(self, overall_goal: str) -> List[Dict[str, str]]:
        """Decomposes goal into specialized worker sub-tasks."""
        subtasks = []
        if "research" in overall_goal.lower() or "find" in overall_goal.lower():
            subtasks.append({"role": "Researcher", "instruction": f"Gather empirical facts for: {overall_goal}"})
        if "code" in overall_goal.lower() or "build" in overall_goal.lower():
            subtasks.append({"role": "Engineer", "instruction": f"Synthesize implementation code for: {overall_goal}"})
        if not subtasks:
            # Default generic worker breakdown
            subtasks.append({"role": "Analyst", "instruction": f"Analyze: {overall_goal}"})
            subtasks.append({"role": "Writer", "instruction": f"Draft summary for: {overall_goal}"})

        return subtasks

    def execute_hierarchy(self, overall_goal: str) -> Dict[str, Any]:
        """Orchestrates task decomposition, parallel/sequential worker execution, and aggregation."""
        subtasks = self.decompose_task(overall_goal)
        worker_results = []

        for st in subtasks:
            role = st["role"]
            worker_fn = self.workers.get(role, lambda inst: f"Executed by {role}: OK")
            output = worker_fn(st["instruction"])
            worker_results.append({
                "role": role,
                "instruction": st["instruction"],
                "output": output
            })

        # Synthesize final output
        summary_lines = [f"- [{r['role']}]: {r['output']}" for r in worker_results]
        final_synthesis = f"Supervisor Synthesis for '{overall_goal}':
" + chr(10).join(summary_lines)

        return {
            "goal": overall_goal,
            "subtasks_executed": len(worker_results),
            "worker_results": worker_results,
            "final_synthesis": final_synthesis
        }
