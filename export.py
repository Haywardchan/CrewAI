import subprocess

try:
    # Run the command and redirect to a text file
    subprocess.run("poetry run financial_analyst_crew > output.txt", shell=True, check=True)

    

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")