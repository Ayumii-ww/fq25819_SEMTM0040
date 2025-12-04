**Vichaya Tedumrongvanich fq25819_SEMTM0040**

# Part 1 - FlowerShop Simulator (SEMTM0040)

FlowerShop Simulator is project for the SEMTM0040 summative assessment. 
The program models a small flower shop that runs over a user-chosen number of months. Each month the owner (Player) to decide how many florists to employ and how many of each bouquet to sell. The simulation then checks labour and supply constraints, updates the shop's cash balance based on income and costs, applies depreciation on supply, restocks supplies fully, and checks whether the shop has gone bankrupt.

The code is structured using Object-oriented design with each major part of the business represented by its own class:

- FlowerShop - main controller of the simulation
- Florist - represents employees and calculates labour time and salary
- Bouquet - defines bouquet types, recipes, prices, and demand
- Greenhouse - tracks inventory, depreciation, and restocking
- main.py - user interaction, game flow, and overall simulation logic

## Files and Class structure 

### main.py 

main.py is the entry point of program and contains the overall game loop and all user interaction with the program. Key responsibilities: 

- Prompting the user for: 
  - Number of months to simulate
  - Initial florist at the start of the simulation
  - Monthly hiring and firing decisions
  - Monthly production plan
-  Calling methods on the FlowerShop objects:
   -  Check supply and labour constraints
   -  Run the end-of-month financial calculation
   -  Fully restock the greenhouse
   -  Handle Bankruptcy with bank loan extension choice
- Print summaries at end of each month (income, costs, balance, current staff and greenhouse supply left)

It does not store business logic inside the file, but delegates work to class which help to keeps the system modular and easier to maintain and readable.

### FlowerShop,py

This is core controller of the simulation. It act as coordinates with other components:

Key responsbiilities:
- HOlding list of florists
- Store bouquet objects
- Track the cash balance
- Check supply constraints
- Check labour constraints
- Process monthly fixed cost (rent, salaries, greenhouse)
- Produce bouquets by consuming greenhouse supply
- Calculate monthly income
- Restock the greenhouse
- Determining bankruptcy 
- Loan system with interest and repayments ---> Extension

This class ensure that every monthly action has economic consequence

### Florist.py  ---> Employee Behaviour and labour working time

Each florist represent as object with
- name
- speciality (optional) ---> Extension
- method to compute monthly labour minutes
- method to compute monthly salary
- method to adjust labor time if the florist specialises in the bouquet type being produce

This class isolates all labour-related logic 

### Bouquet.py ---> Bouquet Types, Recipes and Demand 

Each bouquet type has:

- A unique name
- Ingrediant requirement (greenery, roses, daisies)
- Preparation time in minutes
- Selling price
- Monthly demand limit

These describe the products that sell in shop. The simulation should still work even add new recipes or type of bouquets later

### Greenhouse.py ----> Inventory, Costs, Depreciation


This class stores and manages flower supplies
- Current stock levels
- Monthly depreciation of flowers
- Monthly greenhouse cost based on inventory
- Consuming suppliyes during production
- Restcking to maximum capacity
- Minimum supply checking before production

This keep greenhouse logic in own class to prevents duplication of cost-related formulats and ensure that can track inventory accurately 

## Design Choices and Deabtes

1. Mismatched proportions 

This instruction design aspect is that the maximum monthly demand for all bouquets together can exceed what the shop can give (supply) by having fixed labor caparicty of the florits and greenhouse maximum stock.


# Part 2: Reddit Data Analysis

Required Libraries and External 

This part of coursework uses Python along with several external libraries that are not part of standard Python installation. To successfully run all scripts and Jupyter notebook, you must install the following packages: 

- requests - for retrieving Reddit data through HTTP requests
- pandas - for data manipulation and cleaning
- numpy - for visualisations
- matplotlib - for visubalisation plot graph
- seaborn - for enhance plot graph visualisation
- nltk - for natural langauge processing (tokenisation, stopwords, VADER sentiment analysis)
- scipy - for statistical test 
-  statsmodel - for building regression models

## **Installation Instruction**

## Step 1. To install all required packages:

**Mac/Linux**

'''
%pip install requests pandas numpy matplotlib nltk seaborn statsmodels scipy
'''

Or 

**Window (Command Prompy/Powershell)**

'''
pip install requests pandas numpy matplotlib nltk seaborn statsmodels scipy
'''

## Step 1.5 **Fixing NLTK SSL Certificate Errors 

In case you get errors like:

'''
CERTIFICATE_VERIFY_FAILED
Error loading vader_lexicon
Error loading stopwords
'''

Run this before downloading NLTK corpora: 

'''
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
'''

Then Downloand required NLTK corpora:

'''
import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
'''

These are for 
- **Sentiment Analysis**
- **Stopword removal**
- **Tokenization**

## Step 2. Required NLTK download 

'''
import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
'''

If SSL fails, apply **Step 1.5**

## Step 3. Running the Notebook

This project uses only standard Python libraries and public open source:

- NLTK
- VADER Sentiment Analyzer (Hutto & Gilbert, 2014)
- Request library
- Matplotlib and Seaborn
- Statsmodels 
- Scipy



