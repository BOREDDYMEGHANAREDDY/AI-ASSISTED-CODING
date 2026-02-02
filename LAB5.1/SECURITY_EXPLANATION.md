# Secure User Storage System - Security Explanation

## Overview
This program stores user credentials securely using **bcrypt password hashing**. Passwords are never stored in plain text.

---

## Why Hashing is Secure

### 1. **One-Way Function**
- Hashing is a **one-way operation** - you cannot decrypt a hash back to the original password
- Even if someone accesses the database, they cannot retrieve the actual passwords
- Formula: `hash(password)` → hashed value (irreversible)

```
Plain password: "MyPassword123!"
Hashed result: $2b$12$7FmOxe2E9Zx5K3qPvW1Q7eKL9mN2oP3qR4sT5uV6wX7yZ8aB9cD0e
↑ Cannot convert this back to plain password
```

### 2. **Why Not Other Methods?**

❌ **Plain Text Storage**
```python
# NEVER DO THIS!
users['john@email.com'] = {'password': 'MyPassword123!'}
```
- If database is hacked, passwords are exposed
- Attackers can immediately access user accounts

❌ **Simple Hashing (MD5, SHA1)**
```python
import hashlib
hashed = hashlib.md5('MyPassword123!'.encode()).hexdigest()
# Result: 7e4a8a8d9c4b5e1f3a2c8d5b1e7f9a4c
```
- Fast hashing is vulnerable to **rainbow table attacks**
- Attackers precompute hashes of common passwords
- Same password always produces same hash (vulnerable to pattern recognition)

### 3. **Why Bcrypt is Superior**

✅ **Bcrypt Features:**

| Feature | Benefit |
|---------|---------|
| **Salt** | Random data added to password before hashing; same password creates different hashes |
| **Rounds** | Configurable computation rounds (default: 12); increases time needed for brute force |
| **Adaptive** | Becomes slower as computers get faster; future-proof |
| **Industry Standard** | Widely used in production systems |

```python
# Each registration produces different hash for same password
password = "MyPassword123!"
hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
# $2b$12$abc123xyz789... (different every time)

hash2 = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
# $2b$12$def456uvw012... (different from hash1)

# But verification still works
bcrypt.checkpw(password.encode(), hash1)  # True
bcrypt.checkpw(password.encode(), hash2)  # True
```

### 4. **Attack Scenarios**

#### Scenario A: Database Breach with Plain Text
```
Attacker accesses database:
{
  "john@email.com": "MyPassword123!",
  "jane@email.com": "SecurePass456$"
}
Result: ✗ Passwords immediately compromised
```

#### Scenario B: Database Breach with Bcrypt
```
Attacker accesses database:
{
  "john@email.com": "$2b$12$abc123...",
  "jane@email.com": "$2b$12$def456..."
}
Result: ✓ Passwords are protected
- Attacker cannot reverse the hashes
- Brute force would take years (due to 12 rounds)
- Each hash is unique even for same password
```

---

## Security Features in This Program

### 1. **Password Hashing**
```python
def _hash_password(self, password: str) -> str:
    salt = bcrypt.gensalt(rounds=12)  # Generate random salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')
```

### 2. **Password Verification**
```python
def _verify_password(self, password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
```

### 3. **Password Strength Validation**
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

Example: `SecurePass123!` ✓

### 4. **Email Validation**
- Prevents invalid email formats
- Checks for duplicate registrations

### 5. **Account Deletion Protection**
- Requires password verification before deletion
- Prevents unauthorized account removal

### 6. **No Password Logging**
- Passwords never logged or displayed
- Only hashes are stored in database

---

## Database Structure

```json
{
  "john@email.com": {
    "name": "John Doe",
    "email": "john@email.com",
    "password_hash": "$2b$12$gSvqqUPvlXP2tfVFaWK1Be1DlH.PKZbv5H8KnzzVgXXbVxzy70jKm"
  },
  "jane@email.com": {
    "name": "Jane Smith",
    "email": "jane@email.com",
    "password_hash": "$2b$12$wN8k7QZ9rT2mK1pL3vX5uZ.WqA0bS8cD9eF1gH2iJ3kL4mN5oP6q"
  }
}
```

**Note:** No passwords are stored, only hashes!

---

## Bcrypt Parameters Explained

```python
salt = bcrypt.gensalt(rounds=12)
```

- **rounds=12**: Number of computational rounds
  - 4 rounds: Very fast (~0.1ms) - used in old systems
  - 12 rounds: Balanced (~0.3s) - recommended for current systems
  - 15 rounds: Secure (~1s) - for high-security applications
  
Higher rounds = harder to brute force, but slower verification

---

## Comparison Table

| Aspect | Plain Text | MD5/SHA1 | Bcrypt |
|--------|-----------|----------|---------|
| Reversible | ✓ (Yes) | ✗ (No) | ✗ (No) |
| Unique per password | N/A | ✓ (Yes) | ✗ (No, uses salt) |
| Salt used | N/A | ✗ (No) | ✓ (Yes) |
| Rainbow table resistant | ✗ (No) | ✗ (No) | ✓ (Yes) |
| Adaptive to hardware | ✗ (No) | ✗ (No) | ✓ (Yes) |
| Industry standard | ✗ (No) | ✗ (Deprecated) | ✓ (Yes) |

---

## Best Practices Implemented

1. ✓ **Never store plain text passwords**
2. ✓ **Use cryptographic hashing (bcrypt)**
3. ✓ **Add salt to prevent rainbow table attacks**
4. ✓ **Use adequate rounds for security**
5. ✓ **Validate passwords before hashing**
6. ✓ **Separate password storage from retrieval**
7. ✓ **Never log passwords**
8. ✓ **Use secure password comparison**

---

## How the Program Protects You

### Registration Process
```
User Input: Password "MyPassword123!"
    ↓
Validate strength (8+ chars, uppercase, lowercase, digit, special)
    ↓
Generate random salt
    ↓
Hash password with salt using bcrypt (12 rounds)
    ↓
Store only hash in database
    ↓
User's password never saved in plain text
```

### Login Process
```
User Input: Password "MyPassword123!"
    ↓
Retrieve stored hash from database
    ↓
Hash input with stored salt
    ↓
Compare hashes (bcrypt.checkpw)
    ↓
Grant access if match
    ↓
Actual password never compared directly
```

---

## Security Assumptions & Limitations

✓ **What this protects:**
- Passwords from database theft
- Common passwords from dictionary attacks
- Rainbow table attacks

⚠ **What this doesn't protect:**
- Passwords from keyloggers on user's device
- Weak user passwords (though we enforce strong ones)
- Man-in-the-middle attacks (should use HTTPS/SSL in production)
- Server-side vulnerabilities in authentication logic

---

## Installation & Usage

```bash
# Install required package
pip install bcrypt

# Run the program
python user_storage.py
```

---

## References

- [OWASP: Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Bcrypt Documentation](https://en.wikipedia.org/wiki/Bcrypt)
- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
