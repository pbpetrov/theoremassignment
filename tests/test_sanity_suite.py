import unittest
from tests.home.create_account_test import CreateAccountTest
from tests.home.signin_test import SigninTests
from tests.home.browse_clothes_departments_test import BrowseClothesDepartments
from tests.home.purchase_item_test import PurchaseItemTests


tc1 = unittest.TestLoader().loadTestsFromTestCase(CreateAccountTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SigninTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(BrowseClothesDepartments)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PurchaseItemTests)

sanityTest = unittest.TestSuite([tc1, tc2, tc3, tc4])

unittest.TextTestRunner(verbosity=2).run(sanityTest)
