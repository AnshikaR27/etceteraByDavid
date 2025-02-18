
def main():
    balance = 0 #this approach would not work because yeh variable phir wapas is only accessible in the main function; will not be accessible to the deposit and the withdraw function
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    balance += n

def withdraw(n):
    balance -= n

if __name__ == "__main__":
    main()
