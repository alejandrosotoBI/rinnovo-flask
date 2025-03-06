from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import base64
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv('DB_NAME'), 
        user=os.getenv('DB_USER'), 
        password=os.getenv('DB_PASSWORD'), 
        host=os.getenv('DB_HOST'), 
        port=os.getenv('DB_PORT')
    )


@app.route('/api/gallery', methods=['GET'])
def get_gallery():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get images from the database based on category
    query = "SELECT id, category, name, image, thumbnail FROM images"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    gallery = {"cocinas": [], "closets": [], "centros": []}
    
    for row in rows:
        image_id, category, name, image, thumbnail = row
        
        # Convert image and thumbnail to base64 strings
        image_base64 = base64.b64encode(image).decode('utf-8') if image else None
        thumbnail_base64 = base64.b64encode(thumbnail).decode('utf-8') if thumbnail else None
        
        gallery[category].append({
            "id": image_id,
            "category": category,
            "name": name,
            "image": f"data:image/jpeg;base64,{image_base64}" if image_base64 else "",
            "thumbnail": f"data:image/jpeg;base64,{thumbnail_base64}" if thumbnail_base64 else ""
        })
    
    cursor.close()
    conn.close()
    
    return jsonify(gallery)

if __name__ == '__main__':
    app.run(debug=True)
