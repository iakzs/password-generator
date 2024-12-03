from flask import Flask, render_template, request, jsonify
import string
import secrets

app = Flask(__name__)

def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                     use_numbers=True, use_symbols=True, exclude_similar=False):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    
    # Remove similar characters if requested
    if exclude_similar:
        similar_chars = 'Il1O0'
        lowercase = ''.join(c for c in lowercase if c not in similar_chars.lower())
        uppercase = ''.join(c for c in uppercase if c not in similar_chars.upper())
        numbers = ''.join(c for c in numbers if c not in similar_chars)

    # Build character pool based on options
    pool = ''
    if use_lowercase:
        pool += lowercase
    if use_uppercase:
        pool += uppercase
    if use_numbers:
        pool += numbers
    if use_symbols:
        pool += symbols

    if not pool:
        return None

    # Generate password
    password = ''.join(secrets.choice(pool) for _ in range(length))
    
    # Ensure at least one character from each selected type
    chars = []
    if use_lowercase:
        chars.append(secrets.choice(lowercase))
    if use_uppercase:
        chars.append(secrets.choice(uppercase))
    if use_numbers:
        chars.append(secrets.choice(numbers))
    if use_symbols:
        chars.append(secrets.choice(symbols))
    
    if chars:
        # Replace first few characters with required types
        password_list = list(password)
        for i, char in enumerate(chars):
            password_list[i] = char
        # Shuffle to avoid predictable positions
        secrets.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)

    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    
    try:
        password = generate_password(
            length=int(data.get('length', 12)),
            use_uppercase=data.get('uppercase', True),
            use_lowercase=data.get('lowercase', True),
            use_numbers=data.get('numbers', True),
            use_symbols=data.get('symbols', True),
            exclude_similar=data.get('excludeSimilar', False)
        )
        
        if password is None:
            return jsonify({'error': 'Please select at least one character type'}), 400
            
        return jsonify({'password': password})
    except ValueError:
        return jsonify({'error': 'Invalid parameters'}), 400

if __name__ == '__main__':
    app.run(debug=True)
