# Secure User Storage System

A secure user management system that stores user credentials with bcrypt password hashing.

## Features

✓ **Secure Password Storage**
- Uses bcrypt hashing (never plain text)
- Unique salt for each password
- 12-round computation for strong security

✓ **User Management**
- Register new users with email validation
- Login with password verification
- View user information
- List all users
- Delete accounts with verification

✓ **Password Strength**
- Minimum 8 characters
- Requires uppercase, lowercase, digits, and special characters
- Email format validation
- Duplicate email prevention

✓ **Error Handling**
- Input validation
- Database error handling
- Clear error messages

## Installation

```bash
# Install dependencies
pip install -r requirements_user_storage.txt
```

Or manually:
```bash
pip install bcrypt
```

## Usage

```bash
python user_storage.py
```

## Menu Options

```
1. Register a new user
   - Create account with name, email, password
   - Password is hashed using bcrypt
   
2. Login
   - Verify credentials with stored hash
   - No plain text password comparison
   
3. View user information
   - Retrieve user details (excluding password)
   
4. List all users
   - See all registered users
   
5. Delete account
   - Remove account after password verification
   
6. Exit
   - Close the application
```

## Example Usage

```
--- Register New User ---
Enter full name: John Doe
Enter email: john@example.com
Enter password: SecurePass123!
Success: User 'John Doe' registered successfully.

--- User Login ---
Enter email: john@example.com
Enter password: SecurePass123!
Success: Welcome back, John Doe!
```

## Password Requirements

Password must contain:
- ✓ At least 8 characters
- ✓ At least one uppercase letter (A-Z)
- ✓ At least one lowercase letter (a-z)
- ✓ At least one digit (0-9)
- ✓ At least one special character (!@#$%^&* etc.)

Valid examples: `MySecure123!`, `Password@456`, `SecurePass123!`

## Database Structure

Users are stored in `users.json`:
```json
{
  "john@email.com": {
    "name": "John Doe",
    "email": "john@email.com",
    "password_hash": "$2b$12$..." 
  }
}
```

**Only the hash is stored, never the plain password!**

## Security Features

### Why Bcrypt?

1. **One-Way Hashing**: Cannot reverse the hash to get password
2. **Salt**: Each password gets unique salt, preventing rainbow table attacks
3. **Rounds**: 12 computational rounds make brute force attacks impractical
4. **Adaptive**: Security automatically increases as computers get faster

### How It Protects You

| Scenario | Protection |
|----------|-----------|
| Database stolen | Passwords cannot be recovered (only hashes) |
| Rainbow table attack | Salt makes rainbow tables ineffective |
| Brute force attack | 12 rounds delay each attempt by ~0.3 seconds |
| Pattern recognition | Different hash for each password instance |

### What It Doesn't Protect

- ✗ Keyloggers on user's device
- ✗ Weak user passwords (we enforce strong ones)
- ✗ Man-in-the-middle attacks (use HTTPS in production)

## Technical Details

### Bcrypt Hash Format

```
$2b$12$gSvqqUPvlXP2tfVFaWK1Be1DlH.PKZbv5H8KnzzVgXXbVxzy70jKm
├─ $2b$ : Bcrypt algorithm identifier
├─ 12 : Number of computational rounds
├─ gSvqqUPvlXP2tfVFaWK1Be1 : Salt (22 characters)
└─ DlH.PKZbv5H8KnzzVgXXbVxzy70jKm : Hash (31 characters)
```

### Rounds Explanation

```python
rounds=12  # Recommended for 2024+
- Hash time: ~0.3 seconds
- Brute force 1000 passwords: 5 minutes
- Rainbow table generation: Impractical
```

## Files

- `user_storage.py` - Main application
- `users.json` - User database (auto-created)
- `requirements_user_storage.txt` - Dependencies
- `USER_STORAGE_README.md` - This file
- `SECURITY_EXPLANATION.md` - Detailed security explanation

## Common Issues

**Q: Password requirements too strict?**
A: Yes, intentionally! Strong passwords are crucial for account security.

**Q: Can I recover a lost password?**
A: No, passwords are irreversibly hashed. Implement a "forgot password" with email verification in production.

**Q: Is 12 rounds slow?**
A: ~0.3 seconds per hash is acceptable. Higher security than faster hashing.

**Q: Can I change password?**
A: Current version doesn't have this feature. Would require adding a "change password" option.

## Production Considerations

For production systems, also implement:

1. **HTTPS/SSL** - Encrypt data in transit
2. **Password Reset** - Email-based recovery (don't store temporary passwords)
3. **Rate Limiting** - Limit failed login attempts
4. **Logging** - Log authentication events (not passwords)
5. **2FA** - Two-factor authentication
6. **Database Encryption** - Encrypt database file at rest
7. **CSRF Protection** - Prevent cross-site request forgery
8. **Input Sanitization** - Additional validation

## References

- [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Bcrypt Wikipedia](https://en.wikipedia.org/wiki/Bcrypt)
- [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/)
