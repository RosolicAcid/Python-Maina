# Clean Code — 7 Tips

### Summary of Writing Clean Functions (with Python Examples)

Writing clean functions makes your code easier to read, maintain, and debug. Here are 7 simple rules to follow:

---

### 1. **Keep Your Functions Small**

A function should do only **one thing** and do it well. If it’s too long or does multiple tasks, break it down.

### ❌ Bad Example:

```python
python
CopyEdit
def process_order(order):
    validate_order(order)
    update_inventory(order)
    send_email_notification(order)
    log_order(order)

```

This function does **too many things**!

### ✅ Good Example:

```python
python
CopyEdit
def validate_order(order):
    # Check if order is valid
    pass

def update_inventory(order):
    # Reduce stock quantity
    pass

def send_email_notification(order):
    # Notify user
    pass

```

Each function now has a **single responsibility**.

---

### 2. **Use Meaningful Function Names**

Good names make code **self-explanatory**.

### ❌ Bad Example:

```python
python
CopyEdit
def do_it(a, b):
    return a * b

```

The name "do_it" gives **no clue** what it does.

### ✅ Good Example:

```python
python
CopyEdit
def calculate_area(length, width):
    return length * width

```

Now, it’s clear that this function **calculates the area** of a rectangle.

---

### 3. **Limit the Number of Parameters**

Too many parameters make a function **hard to understand**.

### ❌ Bad Example:

```python
python
CopyEdit
def create_user(name, age, email, country, phone, is_admin, is_verified):
    pass

```

This function has **too many parameters**, making it confusing!

### ✅ Good Example:

```python
python
CopyEdit
class User:
    def __init__(self, name, age, email, country, phone):
        self.name = name
        self.age = age
        self.email = email
        self.country = country
        self.phone = phone

def create_user(user, is_admin=False, is_verified=False):
    pass

```

Now, the user details are grouped into a class, **reducing** the number of parameters.

---

### 4. **Reduce Nesting by Returning Early**

Deeply nested `if` statements **make code harder to read**.

### ❌ Bad Example:

```python
python
CopyEdit
def check_age(age):
    if age >= 18:
        print("Access granted")
    else:
        print("Access denied")

```

Too many conditions can be **avoided**.

### ✅ Good Example:

```python
python
CopyEdit
def check_age(age):
    if age < 18:
        print("Access denied")
        return
    print("Access granted")

```

Returning early **reduces unnecessary nesting**.

---

### 5. **Write Pure Functions (No Side Effects)**

A **pure function** always gives the **same output** for the **same input** and does not modify anything outside itself.

### ❌ Bad Example (Impure function):

```python
python
CopyEdit
discount = 10

def apply_discount(price):
    return price - discount

```

This function **depends on external data** (`discount`), which may change.

### ✅ Good Example (Pure function):

```python
python
CopyEdit
def apply_discount(price, discount):
    return price - discount

```

Now, it **only depends on its inputs**.

---

### 6. **Avoid Boolean Parameters**

Boolean parameters (`True/False`) **make function calls unclear**.

### ❌ Bad Example:

```python
python
CopyEdit
def send_email(user, is_admin):
    if is_admin:
        print(f"Sending admin email to {user}")
    else:
        print(f"Sending user email to {user}")

```

When calling the function, it’s **unclear** what `True` or `False` means.

```python
python
CopyEdit
send_email("Alice", True)   # What does 'True' mean?
send_email("Bob", False)    # What does 'False' mean?

```

### ✅ Good Example (Using Enum):

```python
python
CopyEdit
from enum import Enum

class UserType(Enum):
    ADMIN = "admin"
    USER = "user"

def send_email(user, user_type: UserType):
    if user_type == UserType.ADMIN:
        print(f"Sending admin email to {user}")
    else:
        print(f"Sending user email to {user}")

send_email("Alice", UserType.ADMIN)
send_email("Bob", UserType.USER)

```

Now, the function calls are **self-explanatory**.

---

### 7. **Use Comments Sparingly**

Instead of writing **too many comments**, improve function and variable names.

### ❌ Bad Example (Too many comments):

```python
python
CopyEdit
def c(a, b):
    # This function adds two numbers
    return a + b

```

This comment is **unnecessary** because the function name is unclear.

### ✅ Good Example:

```python
python
CopyEdit
def add_numbers(a, b):
    return a + b

```

Now, the function **explains itself**.

---

### Summary

- **Keep functions small** (each should do only one thing).
- **Use meaningful names** (avoid generic names like `do_it`).
- **Limit parameters** (use objects instead).
- **Reduce nesting** (return early).
- **Write pure functions** (no side effects).
- **Avoid boolean flags** (use Enums instead).
- **Use comments only when necessary** (improve naming instead).

By following these rules, your code will be **cleaner, easier to maintain, and more readable**. 🚀