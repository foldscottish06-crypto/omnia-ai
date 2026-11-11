from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Gemini API Anahtarini Buraya Yazacaksin
GEMINI_API_KEY = "BURAYA_GEMINI_API_KEY_GELECEK"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash-lite')

@app.route('/ai', methods=['GET', 'POST'])
def proxy():
    user_prompt = request.args.get('q') or (request.json.get('prompt') if request.is_json else None)
    
    if not user_prompt:
        return jsonify({"error": "Soru bulunamadi (q parametresi eksik)"}), 400

    try:
        response = model.generate_content(user_prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
