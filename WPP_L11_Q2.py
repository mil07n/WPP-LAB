import pandas as pd
s = pd.Series (["X","Y","T","Aaba","Baca", "CABA", None, "bird","horse","dog"])
upper = s.str.upper()
lower = s.str.lower()
length = s.str.len()

print("UPPERCASE:\n", upper)
print("\nlower case:\n", lower)
print("\nLength:\n", length)