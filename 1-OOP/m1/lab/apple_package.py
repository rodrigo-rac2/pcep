import random

class PackageTooHeavyError(BaseException):
    def __init__(self, max_weight, current_weight):
        message = f"Error! Total package weight would exceed the limit of {max_weight} with {current_weight:.2f} units."
        super().__init__(message)

class AppleCountExceededError(BaseException):
    def __init__(self, value):
        message = f"Error! Cannot add apple as the order is full: {value} apples."
        super().__init__(message)

class Apple:
    def __init__(self):
        self.weight = random.uniform(0.2, 0.5)

class Package:
    apple_count = 0
    total_weight = 0
    
    def __init__(self, max_weight, max_apple_count):
        self.max_weight = max_weight
        self.max_apple_count = max_apple_count
    
    def add_apple(self, apple):
        if(self.total_weight + apple.weight > self.max_weight):
            raise PackageTooHeavyError(self.max_weight, Package.total_weight + apple.weight)
        if(self.apple_count >= self.max_apple_count):
            raise AppleCountExceededError(Package.apple_count)
        Package.apple_count += 1
        Package.total_weight += apple.weight
        
            
if __name__ == '__main__':
    package = Package(300, 1000)
    while(True):
        new_apple = Apple()
        try:
            print("------")
            print(f"Trying to adding apple with weight: {new_apple.weight:.2f}")
            package.add_apple(new_apple)
        except AppleCountExceededError as e:
            print(e)
            break
        except PackageTooHeavyError as e:
            print(e)
            break
        else:
            print("Apple added successfully.")
            print(f"Apple count: {package.apple_count}")
            print(f"Package weight: {package.total_weight:.2f} units")
    print("--------------------")
    print("Package is full. Final package details:")
    print(f"Apple count: {package.apple_count}")
    print(f"Package weight: {package.total_weight:.2f} units")
        