
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3005"]}})

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def validate_password(password: str, max_attempts: int = 3) -> tuple[bool, list[str]]:
    """Validate a password with up to 3 attempts, returning all errors.

    Criteria:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character from !@#$%^&*

    Args:
        password: Password to validate
        max_attempts: Maximum attempts (default 3, not used in single validation)

    Returns:
        Tuple of (is_valid: bool, errors: list of error messages)
    """
    logger.debug(f"Validating password: {password}")
    if not isinstance(password, str):
        return False, ["Password must be a string"]
    
    errors = []
    special_chars = "!@#$%^&*"
    
    if not password:
        errors.append("Password cannot be empty")
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter")
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit")
    if not any(char in special_chars for char in password):
        errors.append("Password must contain at least one special character (!@#$%^&*)")
    
    is_valid = len(errors) == 0
    logger.debug(f"Validation result: is_valid={is_valid}, errors={errors}")
    return is_valid, errors

@app.route("/api/validate-password", methods=["POST"])
def validate_password_endpoint():
    try:
        logger.debug("Received POST request")
        data = request.get_json()
        logger.debug(f"Request data: {data}")
        password = data.get("password", "")
        attempt = data.get("attempt", 1)
        
        if attempt > 3:
            logger.debug("Max attempts exceeded")
            return jsonify({
                "isValid": False,
                "errors": ["Maximum 3 attempts reached"],
                "attempt": attempt
            }), 200
        
        is_valid, errors = validate_password(password)
        logger.debug(f"Response: isValid={is_valid}, errors={errors}, attempt={attempt}")
        return jsonify({
            "isValid": is_valid,
            "errors": errors,
            "attempt": attempt
        }), 200
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            "isValid": False,
            "errors": [f"Server error: {str(e)}"],
            "attempt": attempt
        }), 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
