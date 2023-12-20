# __SpaceBar__

SpaceBar started out as an individual programming project built during a data engineering programme I attended. The idea is: you arrive at the (fake)) SpaceBar restaurant, on your table there is a tablet device through which you order rounds of drinks and eventually receive your receipt.

## __Running the app__

> This setup works for Windows, commands below may vary for Mac or Linux machines.

## SET UP
#### Virtual Environment

  - Create the virtual environment; first open a terminal an navigate to the root of the directory:
    - run `python -m venv .venv`

  - Activate the virtual environment:
    - `source .venv/Scripts/activate`

#### Requirements

  - Install the package dependencies that allow the app to run:
  `pip -m install requirements.txt`

#### Running the app
  -  To begin running the app, run the below from the root of the project:
  `python -m src.app`