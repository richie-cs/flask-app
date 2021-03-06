from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json



views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@views.route('/', methods=['GET', 'POST'])
# can't get to homepage unless you're logged in
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        # checking if note has more than 1 character
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            # if passes validation add new note into note model
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added', category='success')

    return render_template("home.html", user=current_user)
    
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteID = note['noteID']
    note = Note.query.get(noteID)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
        
    return jsonify({})


