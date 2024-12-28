
# 🎟️ Lottery Ticket Checker

This Python script allows you to check the results of your lottery tickets using the "La Vanguardia" website.

## 📋 Features

- Fetch and parse lottery results.
- Display detailed information about each ticket.
- Simple and straightforward to use.

## 🛠️ Libraries Used

- **pandas**: For handling data in DataFrame format.
- **requests**: To send HTTP requests to the lottery website.
- **BeautifulSoup**: For parsing HTML content.

## 📊 How It Works

1. **Data Preparation**: The script starts by creating a DataFrame of the lottery tickets you want to check.
2. **Fetching Results**: For each ticket, it sends a request to the "La Vanguardia" lottery results page.
3. **Parsing**: The script uses BeautifulSoup to parse the HTML and extract the ticket results and details.
4. **Displaying Results**: Finally, it compiles the results into a new DataFrame and prints it.

## 🚀 Getting

