# Best Estimate Price

First coding API after running models on a real estate database

---

# Table of Contents

1. [Overview](#overview)
2. [How to Run](#how-to-run)
3. [9. Transactions in High-Income Cities](#9-transactions-in-high-income-cities)
4. [Notes](#notes)

---

## Overview

- The API is flexible for different cities and years. This project is a Python and SQL library for dealing with data availible for a real estate agency. The objective is to create requests allowing an agency responsible to best estimate its prices per square meters

## How to Run

- Ensure FastAPI and Uvicorn are installed (pip install) / SQL / Python 3.12
- Run the server using `uvicorn app --reload`, assuming the script is named `main.py`.
- Access the API at `http://localhost:8000`
- Use VScode via Anaconda
- DataBase needed downloaded from
  https://www.kaggle.com/datasets/benoitfavier/immobilier-france/data
- data cleaned are on 'Ile de France' with square meters up to 30000€ are out.
- the API gives results based on only one model Random Forest

---

Main entries

- function to validate year entry : validate_year(year: str) => will return an error detail in case the year is not a 4 digit number
- function to validate an integer entry : validate_number(n: str) => will return an error detail in case the text indicates other than an integer
- function to validate an building type entry : validate_building_type(building_type: str) => will return an error detail in case the text is not 'appartement' or 'maison'
- under construction : function to validate the asked data exists in database => validate_existing_data => will return an error detail in case the text is not in the table(s)

---

## Different steps

---

### 1. Average income

---

## Notes

- The database sample used is `Chinook.db`.
- Comprehensive error handling is implemented.

---

## Usage

internal usage only. for training only

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

---
