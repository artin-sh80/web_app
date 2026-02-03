import time

class CoolProject:
    def __init__(self):
        self.status = "Initialized"

    def do_amazing_thing(self):
        """Simulate doing something amazing."""
        self.status = "Working on amazing thing..."
        time.sleep(2)  # Simulate some processing time
        self.status = "Success! You've done an amazing thing!"
        return self.status

# Initialize the cool project
cool_project = CoolProject()

# Perform an amazing thing and print the result
if __name__ == "__main__":
    print("Starting the amazing process...")
    result = cool_project.do_amazing_thing()
    print(result)
