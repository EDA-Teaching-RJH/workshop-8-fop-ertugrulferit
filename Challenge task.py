from ___ import is_valid_email

try:
 assert is_valid_email("sneaky@@kent.ac.uk") == False
except AssertionError:
 print("Warning: A sneaky email bypassed the REGEX!")