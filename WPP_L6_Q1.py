class Password_Manager:
   def __init__(self):
        self.old_passwords = []
   def get_password(self):
        return self.old_passwords[-1] if self.old_passwords else None
   def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False
   def is_correct(self, password):
        return password == self.get_password()
pm = Password_Manager()
print(pm.set_password("ABC123"))  # True
print(pm.set_password("XYZ6fwfw91"))  #True
print(pm.set_password("ABC123"))# False (Already used)
print("Current password:", pm.get_password())#xyz691
print(pm.is_correct("XYZ691"))
print(pm.is_correct("ABC123"))