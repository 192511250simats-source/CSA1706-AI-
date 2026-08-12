Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Vacuum Cleaner Problem
... 
... room = input("Enter room (A/B): ")
... status = input("Enter status (Clean/Dirty): ")
... 
... if status == "Dirty":
...     print("Room", room, "is Dirty")
...     print("Vacuum cleaner is cleaning...")
...     print("Room", room, "is now Clean")
... else:
...     print("Room", room, "is already Clean")
... 
