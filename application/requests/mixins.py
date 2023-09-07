class UserValidatorMixin:
    def validate_email(self):
        if not self.email:
            raise ValueError("E-mail is required")

    def validate_password(self):
        if not self.password:
            raise ValueError("Password is required")

    def validate_confirm_password(self):
        if self.password != self.confirm_password:
            raise ValueError("The passwords don't match")
