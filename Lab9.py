import logging

logging.basicConfig(level=logging.INFO)

def validate_credentials(username, password):
    # Dummy validation logic for demonstration
    # Replace with actual credential validation logic.
    return username == "keni123" and password == "password123"

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    logging.info(f"User {username} attempted to log in.")
    if validate_credentials(username, password):
        logging.info(f"User {username} logged in successfully.")
        return "Login successful"
    else:
        logging.error(f"Failed login attempt for user {username}.")
        return "Invalid credentials"

def logout_user():
    username = input("Enter your username to logout: ")
    logging.info(f"User {username} logged out.")
    return "Logout successful"

def validate_payment_info(user_id, amount):
    # Dummy validation logic for demonstration
    # Replace with actual payment validation logic.
    return amount > 0

def process_payment():
    user_id = input("Enter your user ID: ")
    try:
        amount = float(input("Enter the payment amount: "))
    except ValueError:
        logging.error("Invalid payment amount entered. Amount should be a number.")
        return "Invalid payment amount"

    logging.info(f"Payment process initiated for user {user_id} with amount {amount}.")
    if not validate_payment_info(user_id, amount):
        logging.warning(f"Payment validation failed for user {user_id}.")
        return "Invalid payment details"

    try:
        # Simulate payment processing
        logging.info(f"Payment of {amount} processed successfully for user {user_id}.")
        return "Payment successful"
    except Exception as e:
        logging.error(f"Payment processing error for user {user_id}: {str(e)}")
        return "Payment failed"

def book_accommodation():
    user_id = input("Enter your user ID for booking: ")
    room_type = input("Enter room type (e.g., Single, Double, Suite): ")
    try:
        duration = int(input("Enter the duration of stay (in days): "))
    except ValueError:
        logging.error(f"Invalid duration entered for user {user_id}. Duration should be a number.")
        return "Invalid booking duration"

    logging.info(f"Booking process started for user {user_id}. Room type: {room_type}, Duration: {duration} days.")
    if duration <= 0:
        logging.warning(f"Booking failed for user {user_id} due to invalid duration.")
        return "Invalid duration. Please enter a positive number."

    try:
        # Simulate booking process
        logging.info(f"Booking confirmed for user {user_id}. Room type: {room_type}, Duration: {duration} days.")
        return f"Booking successful: {room_type} room for {duration} days."
    except Exception as e:
        logging.error(f"Booking error for user {user_id}: {str(e)}")
        return "Booking failed"

# Example usage
print(login_user())
print(book_accommodation())
print(process_payment())
print(logout_user())
