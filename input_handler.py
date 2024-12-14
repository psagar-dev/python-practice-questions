class InputHandler:
    
    def getUserInputNumber():
        try:
            return int(input("Enter a number: ").strip())
        except ValueError:
            print("Invalid Input. Please enter a valid integer.")
            return None