from django.db import models

#Creates a class that inherits from models.Model, which allows it to be used as a representation of a database table
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    #Creates an Accounts model manager
    Accounts = models.Manager()

    #Allows specific account references to be returned as owner's name instead of pk
    def __str__(self):
        return self.first_name + ' ' + self.last_name


#Choices for a transaction
TransactionTypes = [('Deposit', 'Deposit'), ('Withdraw', 'Withdraw')]

#Creates a class that inherits from models.Model, which allows it to be used as a representation of a database table
class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    #Creates a Transactions model manager
    Transactions = models.Manager()