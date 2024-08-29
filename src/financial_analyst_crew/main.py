import os
from dotenv import load_dotenv
import sys
load_dotenv()

from src.financial_analyst_crew.crew import FinancialAnalystCrew
def run(query):
    # os.chdir(os.getcwd + '/CrewAi')
    # company_names = [ 'Apple', 'Microsoft', 'IBM']
    # for company in company_names:
    #     FinancialAnalystCrew().crew().kickoff(inputs= {'company_name': company})
    # # TracerProvider issue exist so it is better to do search one by one
    FinancialAnalystCrew().crew().kickoff(inputs= {'company_name': query})
    
def main():
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        print("Please provide a company name as an argument.")

if __name__ == "__main__":
    main()