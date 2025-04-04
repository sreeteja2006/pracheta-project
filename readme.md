💰 Personal Finance Tracker
Hey! This is a small project I made to help keep track of my income and expenses. It's a command-line tool where you can add your daily transactions and check how much you're spending and saving.

🙌 Why I Made This
As a student, I always lose track of where my money goes. So I made this basic finance tracker to manage my money better. It’s simple, easy to use, and runs in the terminal.

🔧 Features
Add income or expense

View all your transactions

Check total income, total expense, and balance

Monthly spending summary (very useful!)

Save and delete transactions

🧑‍💻 How to Use It
Open your terminal or command prompt.

Run the finance_tracker.py file using Python.

A menu will appear—just follow the options to use different features.

Don’t forget to save before exiting so your data stays safe!

📁 What Each File Does
finance_tracker.py
This is the main file that connects everything. It runs the program and saves your data when you exit.

📅 Date Handling (datetime)
I used the datetime module to group expenses by month. It helps in showing how much you spent each month.

Like converting "2025-04-05" into "2025-04" format using:

strptime() – to read the date

strftime("%Y-%m") – to format it for monthly grouping

💾 Storing Data (JSON)
All the transactions are saved in a file called transactions.json.

load_transactions() – loads existing data

save_transactions() – saves all the current data

So even if you close the app, you don’t lose your transactions.

🧑‍💻 Menu & User Input (user_interface.py)
This part shows the menu and handles your inputs. You can:

Add a transaction

Print all transactions

Delete one if needed

View monthly summaries, balance, etc.

🧰 Utility Functions (utils.py)
I added some checks to make sure the input is correct:

validate_date() – checks if the date is in YYYY-MM-DD format

validate_amount() – checks if the amount is a number

🧪 Tests
There are some basic test files in the tests/ folder to check if the important parts work properly. You can run them using Python's unittest module.


You can find the source code and contribute to the project here: [Personal Finance Tracker Repository](https://github.com/sreeteja2006/pracheta-project)

