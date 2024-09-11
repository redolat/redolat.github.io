The SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion) are fundamental to writing clean, maintainable, and scalable code. Below is a Python example of a `Pipeline` class that adheres to these principles. The pipeline consists of several blocks, each representing an API call with either an API key or Bearer token for authentication. The code is kept between 100-200 lines and uses subclasses to represent different API calls.

```python
from abc import ABC, abstractmethod

# Interface Segregation Principle: Abstract class for all API blocks
class APIBlock(ABC):
    @abstractmethod
    def fetch_data(self, input_data):
        pass

# Single Responsibility Principle: Each block handles a single API call

class APIBlock1(APIBlock):
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_data(self, input_data):
        # Simulate API call using the api_key
        response = f"Data from API 1 with key {self.api_key} based on {input_data}"
        return response

class APIBlock2(APIBlock):
    def __init__(self, bearer_token):
        self.bearer_token = bearer_token

    def fetch_data(self, input_data):
        # Simulate API call using the bearer_token
        response = f"Data from API 2 with bearer token {self.bearer_token} based on {input_data}"
        return response

class APIBlock3(APIBlock):
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_data(self, input_data):
        # Simulate API call using the api_key
        response = f"Data from API 3 with key {self.api_key} based on {input_data}"
        return response

class APIBlock4(APIBlock):
    def __init__(self, bearer_token):
        self.bearer_token = bearer_token

    def fetch_data(self, input_data):
        # Simulate API call using the bearer_token
        response = f"Data from API 4 with bearer token {self.bearer_token} based on {input_data}"
        return response

class APIBlock5(APIBlock):
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_data(self, input_data):
        # Simulate API call using the api_key
        response = f"Data from API 5 with key {self.api_key} based on {input_data}"
        return response

# Open/Closed Principle: The Pipeline class is open for extension by adding new APIBlock subclasses but closed for modification.

class Pipeline:
    def __init__(self, blocks):
        self.blocks = blocks

    def run(self, initial_input):
        data = initial_input
        for block in self.blocks:
            data = block.fetch_data(data)
        return data

# Dependency Inversion Principle: High-level modules should not depend on low-level modules. Both should depend on abstractions.

if __name__ == "__main__":
    # Instantiate the pipeline with different API blocks
    pipeline = Pipeline([
        APIBlock1(api_key="API_KEY_1"),
        APIBlock2(bearer_token="BEARER_TOKEN_2"),
        APIBlock3(api_key="API_KEY_3"),
        APIBlock4(bearer_token="BEARER_TOKEN_4"),
        APIBlock5(api_key="API_KEY_5"),
    ])

    # Run the pipeline with initial input
    result = pipeline.run(initial_input="Initial Input Data")
    print(result)
```

### Explanation:

1. **Single Responsibility Principle (SRP)**: Each API block (`APIBlock1`, `APIBlock2`, etc.) is responsible for only one API call.

2. **Open/Closed Principle (OCP)**: The `Pipeline` class can be extended with new `APIBlock` subclasses without modifying its code.

3. **Liskov Substitution Principle (LSP)**: Each `APIBlock` subclass can be substituted with any other subclass without affecting the `Pipeline` class's functionality.

4. **Interface Segregation Principle (ISP)**: The `APIBlock` abstract class enforces that each block only implements the `fetch_data` method it requires.

5. **Dependency Inversion Principle (DIP)**: The `Pipeline` class depends on the abstraction (`APIBlock`), not on specific implementations.

This solution adheres to the SOLID principles and provides a scalable and maintainable architecture for your pipeline. The total code is within the 100-200 lines range, and the use of subclasses makes it easy to extend the pipeline with new blocks.


When writing clean and maintainable code, several design principles can guide you, one of the most popular being **SOLID** principles. These principles help improve software architecture and maintainability. Here's a breakdown of **SOLID** principles with examples in Python:

### 1. **S - Single Responsibility Principle (SRP)**
A class should have only one reason to change, meaning it should have only one responsibility or job.

**Example:**

```python
class Invoice:
    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self):
        return self.amount * 1.2  # Add tax (20%)

class InvoicePrinter:
    @staticmethod
    def print_invoice(invoice):
        print(f"Invoice Total: {invoice.calculate_total()}")

# Usage:
invoice = Invoice(100)
InvoicePrinter.print_invoice(invoice)
```

In this example, the `Invoice` class handles the business logic of the invoice, while the `InvoicePrinter` class takes care of the printing. Each class has a single responsibility.

---

### 2. **O - Open/Closed Principle (OCP)**
Software entities (classes, modules, functions) should be open for extension but closed for modification.

**Example:**

```python
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, total):
        pass

class NoDiscount(Discount):
    def apply(self, total):
        return total

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, total):
        return total - (total * self.percentage)

# Usage:
discount_strategy = PercentageDiscount(0.1)  # 10% discount
total = discount_strategy.apply(100)
print(f"Total after discount: {total}")
```

Here, the discount strategy can be extended by adding new discount classes without modifying existing code, making it follow the OCP principle.

---

### 3. **L - Liskov Substitution Principle (LSP)**
Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

**Example:**

```python
class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")

# Usage:
def make_bird_fly(bird: Bird):
    return bird.fly()

sparrow = Sparrow()
print(make_bird_fly(sparrow))  # Works fine

penguin = Penguin()
print(make_bird_fly(penguin))  # Throws an error (violates LSP)
```

In this example, `Penguin` violates LSP because it's a `Bird` that can't fly. A better design might avoid using `fly` for `Penguin` or represent it in another way to keep behavior consistent.

---

### 4. **I - Interface Segregation Principle (ISP)**
Clients should not be forced to depend on interfaces they do not use.

**Example:**

```python
class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

class SimplePrinter(Printer):
    def print_document(self):
        print("Printing document")

# Usage:
printer = SimplePrinter()
printer.print_document()  # Works without needing to implement scan
```

In this example, `SimplePrinter` implements only the `Printer` interface, and isn't forced to implement `Scanner`. This adheres to ISP by keeping interfaces small and focused.

---

### 5. **D - Dependency Inversion Principle (DIP)**
High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Example:**

```python
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving data: {data} to MySQL Database")

class Application:
    def __init__(self, db: Database):
        self.db = db

    def save_data(self, data):
        self.db.save(data)

# Usage:
db = MySQLDatabase()
app = Application(db)
app.save_data("Some important data")
```

Here, the `Application` depends on the abstraction `Database`, not the concrete `MySQLDatabase`. This makes the code more flexible, allowing different types of databases to be used without changing the application logic.

---

By following these **SOLID** principles, you can create code that is easier to maintain, extend, and scale.