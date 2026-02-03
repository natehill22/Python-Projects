from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


#Renders the Homepage when requested
def home(request):
    form = TransactionForm(data=request.POST or None) #Retrieves Transaction Form
    if request.method == 'POST': #Checks if request method is POST
        pk = request.POST['account'] #If form is submitted, retrieve specific account the user want to view
        return balance(request, pk) #Calls balance function to render that account's Balance Sheet
    content = {'form': form} #Passes form content to the template as a dictionary
    return render(request, 'checkbook/index.html', content) #Adds content of form to page

#Renders the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) #Retrieves Account Form
    if request.method == 'POST': #Checks if request method is POST
        if form.is_valid(): #Checks to see if the submitted form is valid and if so, saves the form
            form.save() #Saves new account
            return redirect('index') #Returns user back to homepage
    content = {'form': form} #Saves form content to the template as a dictionary
    return render(request, 'checkbook/CreateNewAccount.html', content) #Adds content of form to page

#Renders the Balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) #Setting the account variable to the value of the dB's Account model using the particular record taken from the URL before, if errors, show a 404
    transactions = Transaction.Transactions.filter(account=pk) #Retrieves all accounts' transactions
    current_total = account.initial_deposit #Creates account total variable, that starts with initial deposit amount
    table_contents = {} #Creates dictionary into which transaction info will be put
    for t in transactions: #Loop through transactions and determine which is a deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount #If type is a deposit, add amount to total balance
            table_contents.update({t: current_total}) #Add transaction and total to the dictionary
        else:
            current_total -= t.amount #If type is a withdrawal, subtract amount from total balance
            table_contents.update({t: current_total}) #Add transaction and total to the dictionary
    #Pass account, account total balance, and transaction info to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

#Renders the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # Retrieves Transaction Form
    if request.method == 'POST':  #Checks if request method is POST
        if form.is_valid():  #Checks to see if the submitted form is valid and if so, saves the form
            pk = request.POST['account'] #Retrieve which account the transaction was for
            form.save()  #Saves the transaction form
            return balance(request, pk)  #Returns user to that user's specific balance sheet
    content = {'form': form}  #Saves form content to the template as a dictionary
    return render(request, 'checkbook/AddTransaction.html', content)  #Adds content of form to page

