#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewaisearcher.crew import Crewaisearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def load_html_template():
    with open('src/crewaisearcher/config/html_template.html', 'r') as file:
        html_template = file.read()
    return html_template

def run():
    """
    Run the crew.
    """
    global inputs
    
    inputs = {
        'car': input("Qual o seu veículo?"),
        'hp': int(input("Qual a quantidade de HP's requeridos?")),
        'html_template': load_html_template(),
        'current_year': str(datetime.now().year)
    }

    
    
    try:
        Crewaisearcher().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "car": input("Qual o seu veículo"),
        'hp': int(input("Qual a quantidade de HP's requeridos?")),
        'html_template': load_html_template(),
        'current_year': str(datetime.now().year)
    }
    try:
        Crewaisearcher().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Crewaisearcher().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "car": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Crewaisearcher().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
