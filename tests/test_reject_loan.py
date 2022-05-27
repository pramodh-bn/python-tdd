from app.loan import Loan
from app.reject_loan import reject_loan

def test_rejecT_loan():
    loan = Loan(amount=100_000)

    assert not reject_loan(loan).rejected()