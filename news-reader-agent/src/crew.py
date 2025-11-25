from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class TranslatorCrew:
    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def ko2en_agent(self):
        return Agent(
            config=self.agents_config["ko2en_agent"],  # type: ignore[index]
        )

    @agent
    def en2ko_agent(self):
        return Agent(
            config=self.agents_config["en2ko_agent"],  # type: ignore[index]
        )

    @task
    def ko2en(self):
        return Task(
            config=self.tasks_config["ko2en_task"],  # type: ignore[index]
        )

    @task
    def en2ko(self):
        return Task(
            config=self.tasks_config["en2ko_task"],  # type: ignore[index]
        )

    @crew
    def assemble_crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
