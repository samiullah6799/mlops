from main import Wallet

wallet = Wallet(2000)

def test_getAmount():
	assert wallet.getAmount() == 2000

def test_deposit():
	assert wallet.deposit(2000) == 4000

def test_withdraw():
	assert wallet.withdraw(2000) == 2000

def test_getName():
	assert wallet.getName() == "This is Wallet Class"
