import os
from dotenv import load_dotenv
load_dotenv()

from financial_analyst_crew.crew import FinancialAnalystCrew

def run():
    company_names = [ 'Apple', 'Microsoft', 'IBM']
    for company in company_names:
        FinancialAnalystCrew().crew().kickoff(inputs= {'company_name': company})


if __name__ == "__main__":
    run()