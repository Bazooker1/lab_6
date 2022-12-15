from app import app
import constants
from flask import render_template, request
@app.route('/', methods=['GET'])
def index():

    name = None
    gender = None
    program_id = -10
    subject_id = []
    olympiad_id = []
    flag = 0

    if (request.values.get('username')):
        name = request.values.get('username')
    if (request.values.get('gender')):
        gender = request.values.get('gender')
    if (request.values.getlist('subject[]')):
        subject_id = request.values.getlist('subject[]')
    if (request.values.getlist('olympiad[]')):
        olympiad_id = request.values.getlist('olympiad[]')

    if (request.values.get('username') and request.values.get('gender') and request.values.getlist('subject[]') and request.values.getlist('olympiad[]')) :
        flag = 1

    subjects_select = [constants.subjects[int(i)] for i in subject_id]
    olympiad_select = [constants.olympiad[int(i)] for i in olympiad_id]

    if (request.values.get('program')):
        program_id = request.values.get('program')
        html = render_template(
            'index.html',
        program_list=constants.programs,
        subject_list=constants.subjects,
        olympiad_list=constants.olympiad,
        name=name,
        gender=gender,
        flag = flag,
        program=constants.programs[int(program_id)],
        subjects_select=subjects_select,
        olympiad_select=olympiad_select,
        len=len
        )
        return html
    else:
        html = render_template(
            'index.html',
            program_list=constants.programs,
            subject_list=constants.subjects,
            olympiad_list=constants.olympiad,
            name=name,
            gender=gender,
            program=program_id,
            flag = flag,
            subjects_select=subjects_select,
            olympiad_select=olympiad_select,
            len=len
        )
        return html