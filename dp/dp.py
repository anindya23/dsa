class Auth:
    pass

class TestAuthentication:
    def test_val_pass(self):
        auth = Auth()
        result = auth.val_password("Ani@#0Roy@")
        self.assertTrue(result)

    def test_pass_too_short(self):
        auth = Auth()
        result = auth.val_pass("Aninidya")
        self.assertFalse(result)

    def test_password_too_long(self):
        auth = Auth()
        result = auth.val_password("This is a $%2323 super lond password and super strong, no doubt.")
        self.assertFalse(result)

    def test_password_no_digits(self):
        auth = Authentication()
        result = auth.val_password("Anindya")
        self.assertFalse(result)

    def test_password_no_special_chars(self):
        auth = Auth()
        result = auth.val_password("Anindya@43")
        self.assertFalse(result)

    def test_password_no_upper_case(self):
        auth = Auth()
        result = auth.val_password("roy3423chy@#")
        self.assertFalse(result)

    def test_password_no_lower_case(self):
        auth = Auth()
        result = auth.val_password("#ANINDYAROYCHY1")
        self.assertFalse(result)

    def test_password_valid(self):
        auth = Auth()
        result = auth.val_password("Comp710@2023")
        self.assertTrue(result)

if __name__ == "__main__":
    pass