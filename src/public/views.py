"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, flash, redirect,url_for, request
from .forms import LogUserForm, secti,masoform, GameUserForm
from ..data.database import db
from ..data.models import LogUser, GameUser
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/secti', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/secti.tmpl', form=form)

@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

@blueprint.route('/gameuserinput',methods=['GET', 'POST'])
def GameUserInput():
    form = GameUserForm()
    if form.validate_on_submit():
        GameUser.create(**form.data)
    return render_template("public/GameUser.tmpl", form=form)

@blueprint.route('/gameuserlist',methods=['GET'])
def Gameuserlist():
    pole = db.session.query(GameUser).all()
    return render_template("public/gameuserlist.tmpl",data = pole)

@blueprint.route('/editgameuser/<int:id>',methods=['GET', 'POST'])
def GameUserEdit(id):
    edituser = db.session.query(GameUser).get(id)
    form = GameUserForm(obj = edituser)
    if form.validate_on_submit():
        edituser.update(**form.data)
        flash("data aktualizovana", category="info")
    return render_template("public/GameUser.tmpl", form=form)

@blueprint.route('/delgameuser/<int:id>',methods=['GET', 'POST'])
def GameUserDel(id):
    edituser = db.session.query(GameUser).get(id)
    db.session.delete(edituser)
    db.session.commit()
    flash("smazano", category="info")
    return redirect(request.args.get('next') or url_for('public.Gameuserlist'))