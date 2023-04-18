from flask import Flask, render_template, request

app = Flask(__name__)

folders = []

@app.route('/')
def home():
    return render_template('home.html', folders=folders)

@app.route('/create_folder', methods=['POST'])
def create_folder():
    folder_name = request.form['folder_name']
    folders.append({'name': folder_name, 'flashcards': []})
    return 'Folder created successfully.'

@app.route('/delete_folder', methods=['POST'])
def delete_folder():
    folder_name = request.form['folder_name']
    for folder in folders:
        if folder['name'] == folder_name:
            folders.remove(folder)
            break
    return 'Folder deleted successfully.'

@app.route('/create_flashcard', methods=['POST'])
def create_flashcard():
    folder_name = request.form['folder_name']
    card_front = request.form['card_front']
    card_back = request.form['card_back']
    for folder in folders:
        if folder['name'] == folder_name:
            folder['flashcards'].append({'front': card_front, 'back': card_back})
            break
    return 'Flashcard created successfully.'

@app.route('/delete_flashcard', methods=['POST'])
def delete_flashcard():
    folder_name = request.form['folder_name']
    flashcard_index = int(request.form['flashcard_index'])
    for folder in folders:
        if folder['name'] == folder_name:
            del folder['flashcards'][flashcard_index]
            break
    return 'Flashcard deleted successfully.'

@app.route('/edit_flashcard', methods=['POST'])
def edit_flashcard():
    folder_name = request.form['folder_name']
    flashcard_index = int(request.form['flashcard_index'])
    card_front = request.form['card_front']
    card_back = request.form['card_back']
    for folder in folders:
        if folder['name'] == folder_name:
            folder['flashcards'][flashcard_index]['front'] = card_front
            folder['flashcards'][flashcard_index]['back'] = card_back
            break
    return 'Flashcard edited successfully.'

