"""
Secure User Details Storage System
Stores user information with hashed passwords using bcrypt
"""

import bcrypt
import json
import os
import re
from pathlib import Path
from typing import Optional, Dict, Tuple

# Database file to store user data
DATABASE_FILE = "users.json"


class UserManager:
    """
    Manages secure storage and retrieval of user information.
    Passwords are hashed using bcrypt for security.
    """
    
    def __init__(self, db_file: str = DATABASE_FILE):
        """
        Initialize the UserManager.
        
        Args:
            db_file: Path to the JSON file storing user data
        """
        self.db_file = db_file
        self._ensure_database_exists()
    
    def _ensure_database_exists(self):
        """Create database file if it doesn't exist."""
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as f:
                json.dump({}, f)
    
    def _load_users(self) -> Dict:
        """
        Load users from the database file.
        
        Returns:
            Dictionary of users
        """
        try:
            with open(self.db_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading database: {str(e)}")
            return {}
    
    def _save_users(self, users: Dict) -> bool:
        """
        Save users to the database file.
        
        Args:
            users: Dictionary of users to save
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(self.db_file, 'w') as f:
                json.dump(users, f, indent=4)
            return True
        except IOError as e:
            print(f"Error writing to database: {str(e)}")
            return False
    
    def _validate_email(self, email: str) -> bool:
        """
        Validate email format.
        
        Args:
            email: Email address to validate
            
        Returns:
            True if valid, False otherwise
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def _validate_password(self, password: str) -> Tuple[bool, str]:
        """
        Validate password strength.
        
        Args:
            password: Password to validate
            
        Returns:
            Tuple of (is_valid, message)
        """
        if len(password) < 8:
            return False, "Password must be at least 8 characters long."
        
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter."
        
        if not re.search(r'[a-z]', password):
            return False, "Password must contain at least one lowercase letter."
        
        if not re.search(r'[0-9]', password):
            return False, "Password must contain at least one digit."
        
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
            return False, "Password must contain at least one special character."
        
        return True, "Password is strong."
    
    def _hash_password(self, password: str) -> str:
        """
        Hash a password using bcrypt.
        
        Args:
            password: Plain text password
            
        Returns:
            Hashed password (bytes decoded as string)
        """
        # Generate salt and hash the password
        salt = bcrypt.gensalt(rounds=12)  # 12 rounds provides good security/speed balance
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    def _verify_password(self, password: str, hashed_password: str) -> bool:
        """
        Verify a password against its hash.
        
        Args:
            password: Plain text password to check
            hashed_password: Stored hashed password
            
        Returns:
            True if password matches, False otherwise
        """
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        except Exception as e:
            print(f"Error verifying password: {str(e)}")
            return False
    
    def register_user(self, name: str, email: str, password: str) -> Tuple[bool, str]:
        """
        Register a new user with secure password hashing.
        
        Args:
            name: User's full name
            email: User's email address
            password: User's password (will be hashed)
            
        Returns:
            Tuple of (success, message)
        """
        # Validate inputs
        if not name or not name.strip():
            return False, "Error: Name cannot be empty."
        
        if not email or not email.strip():
            return False, "Error: Email cannot be empty."
        
        if not self._validate_email(email):
            return False, "Error: Invalid email format."
        
        if not password:
            return False, "Error: Password cannot be empty."
        
        # Validate password strength
        is_valid, message = self._validate_password(password)
        if not is_valid:
            return False, f"Error: {message}"
        
        # Load existing users
        users = self._load_users()
        
        # Check if email already exists
        if email in users:
            return False, "Error: Email already registered."
        
        # Hash the password
        hashed_password = self._hash_password(password)
        
        # Store user data (password is hashed, never stored in plain text)
        users[email] = {
            'name': name.strip(),
            'email': email.strip(),
            'password_hash': hashed_password  # Only hash is stored
        }
        
        # Save to database
        if self._save_users(users):
            return True, f"Success: User '{name}' registered successfully."
        else:
            return False, "Error: Failed to save user to database."
    
    def login_user(self, email: str, password: str) -> Tuple[bool, str]:
        """
        Authenticate a user by verifying email and password.
        
        Args:
            email: User's email address
            password: User's password
            
        Returns:
            Tuple of (success, message)
        """
        # Validate inputs
        if not email or not password:
            return False, "Error: Email and password are required."
        
        # Load users
        users = self._load_users()
        
        # Check if email exists
        if email not in users:
            return False, "Error: Invalid email or password."
        
        # Retrieve stored password hash
        stored_hash = users[email]['password_hash']
        
        # Verify password
        if self._verify_password(password, stored_hash):
            user_name = users[email]['name']
            return True, f"Success: Welcome back, {user_name}!"
        else:
            return False, "Error: Invalid email or password."
    
    def get_user(self, email: str) -> Optional[Dict]:
        """
        Retrieve user information (excluding password hash).
        
        Args:
            email: User's email address
            
        Returns:
            User data dictionary or None if not found
        """
        users = self._load_users()
        
        if email not in users:
            return None
        
        user = users[email].copy()
        # Don't return the password hash
        del user['password_hash']
        return user
    
    def list_all_users(self) -> list:
        """
        Get list of all registered users (without passwords).
        
        Returns:
            List of user data dictionaries
        """
        users = self._load_users()
        user_list = []
        
        for user_data in users.values():
            user_info = {
                'name': user_data['name'],
                'email': user_data['email']
            }
            user_list.append(user_info)
        
        return user_list
    
    def delete_user(self, email: str, password: str) -> Tuple[bool, str]:
        """
        Delete a user account after password verification.
        
        Args:
            email: User's email address
            password: User's password for verification
            
        Returns:
            Tuple of (success, message)
        """
        # Verify user credentials first
        is_valid, _ = self.login_user(email, password)
        
        if not is_valid:
            return False, "Error: Invalid credentials. Account deletion failed."
        
        users = self._load_users()
        
        if email in users:
            user_name = users[email]['name']
            del users[email]
            
            if self._save_users(users):
                return True, f"Success: User '{user_name}' deleted successfully."
            else:
                return False, "Error: Failed to delete user from database."
        
        return False, "Error: User not found."


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("Secure User Management System")
    print("="*50)
    print("1. Register a new user")
    print("2. Login")
    print("3. View user information")
    print("4. List all users")
    print("5. Delete account")
    print("6. Exit")
    print("="*50)


def main():
    """Main function to run the application."""
    manager = UserManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            # Register new user
            print("\n--- Register New User ---")
            name = input("Enter full name: ").strip()
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            
            success, message = manager.register_user(name, email, password)
            print(message)
        
        elif choice == '2':
            # Login
            print("\n--- User Login ---")
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            
            success, message = manager.login_user(email, password)
            print(message)
        
        elif choice == '3':
            # View user information
            print("\n--- View User Information ---")
            email = input("Enter email: ").strip()
            user = manager.get_user(email)
            
            if user:
                print(f"\nUser Information:")
                print(f"  Name: {user['name']}")
                print(f"  Email: {user['email']}")
            else:
                print("Error: User not found.")
        
        elif choice == '4':
            # List all users
            print("\n--- All Registered Users ---")
            users = manager.list_all_users()
            
            if users:
                for i, user in enumerate(users, 1):
                    print(f"{i}. {user['name']} ({user['email']})")
            else:
                print("No users registered yet.")
        
        elif choice == '5':
            # Delete account
            print("\n--- Delete Account ---")
            email = input("Enter email: ").strip()
            password = input("Enter password for verification: ").strip()
            
            success, message = manager.delete_user(email, password)
            print(message)
        
        elif choice == '6':
            # Exit
            print("\nThank you for using Secure User Management System. Goodbye!")
            break
        
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
