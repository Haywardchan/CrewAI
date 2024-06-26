import os
from dotenv import load_dotenv
load_dotenv()

from financial_analyst_crew.crew import FinancialAnalystCrew

def run():
    # os.chdir(os.getcwd + '/CrewAi')
    # company_names = [ 'Apple', 'Microsoft', 'IBM']
    # for company in company_names:
    #     FinancialAnalystCrew().crew().kickoff(inputs= {'company_name': company})
    # # TracerProvider issue exist so it is better to do search one by one
    FinancialAnalystCrew().crew().kickoff(inputs= {'company_name': '0002.HK'})

if __name__ == "__main__":
    run()