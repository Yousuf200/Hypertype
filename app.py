from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)


easy_words = ["the", "of", "and", "a", "to", "in", "is", "you", "that", "it", "for", "on", "their", "was", "with", "they", "at", "be", "this", "are"]
medium_words = ["communicate", "information", "opportunity", "responsibility", 'at', 'sea', 'fish', 'earth', 'flower', 'animal', 'country', 'question',"comfortable", "experience", "potential", "significant", "challenge", "achieve"]
hard_words = ["cryptocurrency", "cybersecurity",'sun', 'moon', 'river', 'forest', 'picture', 'window', 'building', 'e', 'on', 'star', 'cloud', 'rain', 'snow', 'mountain', 'valley', 'universe', "artificial intelligence", "machine learning", "quantum computing", "self driving car"]

combined_words = easy_words + medium_words + hard_words
random.shuffle(combined_words)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/new_sentence')
def new_sentence():
    sentence = ' '.join(random.choices(combined_words, k=150))
    return jsonify(sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True)
