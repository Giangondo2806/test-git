from asyncio.log import logger
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
app = Flask(__name__)
CORS(app)

#connect tới database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:giangtb@localhost:3306/manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Tắt cảnh báo
db = SQLAlchemy(app)

# Danh sách users (ví dụ)
users = [
    {"id": 1, "username": "john_doe", "email": "john.doe@example.com"},
    {"id": 2, "username": "jane_admin", "email": "jane.admin@example.com"},
    {"id": 3, "username": "peter_user", "email": "peter.user@example.com"}
]

@app.route('/users', methods=['GET'])
def get_users():
    """
    API endpoint trả về danh sách users
    """

    query = "SELECT * FROM users;"
    result = db.session.execute(text(query))
    users_list = []
   

    for row in result:
        user_dict = {
                "id": row[0],
                "username": row[1],
                "password": row[2],
                "email": row[3],
                "name": row[4],
                "123-456-7890": row[5],
                "role": row[6]
            }
        users_list.append(user_dict)

        # return jsonify(users_list)    
    return jsonify(users_list);

@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        full_name = data.get('full_name')
        phone_number = '921232132'
        address = 'phoyen'
        role = 'admin'
        query = f"INSERT INTO `users` (`username`, `password`, `email`, `full_name`, `phone_number`, `address`, `role`) VALUES ('{username}', '{password}', '{email}', '{full_name}', '{phone_number}', '{address}', '{role}')"
        
        print(query)
        
        result = db.session.execute(text(query))
        db.session.commit()
        
    

        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback() # rollback trong trường hợp có lỗi
        logger.error(f"Error when inserting: {e}")
        return jsonify({"error": "Failed to create user"}), 500
    
if __name__ == '__main__':
    app.run(debug=True)