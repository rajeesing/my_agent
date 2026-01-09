from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MyAgent():
    """MyAgent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def legacy_code_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['legacy_code_analyzer'], 
            verbose=True
        )
    
    @agent
    def domain_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['domain_extractor'], 
            verbose=True
        )
    
    @agent
    def tech_debt_assessor(self) -> Agent:
        return Agent(
            config=self.agents_config['tech_debt_assessor'], 
            verbose=True
        )
    
    @agent
    def modernization_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['modernization_advisor'], 
            verbose=True
        )
    @task
    def code_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['legacy_code_analyzer_task'],
        )
    @task
    def domain_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['domain_extractor_task'], 
        )
    @task
    def tech_debt_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['tech_debt_assessor_task'], 
        )
    @task
    def modernization_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['modernization_advisor_task'], 
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MyAgent crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            output_log_file="my_agent_crew_output.log",
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
