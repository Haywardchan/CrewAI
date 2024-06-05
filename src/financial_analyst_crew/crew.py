from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from langchain_groq import ChatGroq
from langchain.llms import Ollama
import yaml
import os
Ollama_mixtral = Ollama(model = "mixtral")
# os.environ['OPENAI_API_KEY'] = ''

@CrewBase
class FinancialAnalystCrew():

    def __init__(self) -> None:
        self.agents_config = self.load_config('/src/financial_analyst_crew/config/agents.yaml')
        self.tasks_config = self.load_config('/src/financial_analyst_crew/config/tasks.yaml')
        self.groq_llm = Ollama_mixtral

    def load_config(self, file_path):
        with open(os.getcwd() + file_path, 'r') as f:
            return yaml.safe_load(f)

    @agent
    def company_researcher(self) -> Agent:
        return Agent(
            config = self.agents_config['company_researcher'],
            llm = self.groq_llm
        )
    
    @agent
    def company_analyst(self) -> Agent:
        return Agent(
            config = self.agents_config['company_analyst'],
            llm = self.groq_llm
        )
    
    @task
    def research_company_task(self) -> Task:
        return Task(
            config = self.tasks_config['research_company_task'],
            agent = self.company_researcher()
        )
    
    @task
    def analyze_company_task(self) -> Task:
        return Task(
            config = self.tasks_config['analyze_company_task'],
            agent = self.company_analyst()
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = [self.company_analyst(), self.company_researcher()],
            tasks = [self.research_company_task(), self.analyze_company_task()],
            process = Process.sequential,
            full_output = True,
            verbose = 2
        )