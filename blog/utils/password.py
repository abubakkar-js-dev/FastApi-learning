from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


class Hash():
    def hash_password(password: str) -> str:
        """Hash a password"""
        return pwd_context.hash(password)
    
    def verify_password(plain_pass: str, hashed_pass: str) -> bool:
        """Verify a passowrd against a hash"""
        return pwd_context.verify(plain_pass,hashed_pass)