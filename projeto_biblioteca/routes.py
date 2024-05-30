from flask import render_template, request, redirect, url_for
from projeto_biblioteca import app, db
from projeto_biblioteca.models import Livro

@app.route('/')
def index():
    livros = Livro.query.all()
    return render_template('index.html', livros=livros)

@app.route('/adicionar_livro', methods=['GET', 'POST'])
def adicionar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano_publicacao = request.form['ano_publicacao']
        novo_livro = Livro(titulo=titulo, autor=autor, ano_publicacao=ano_publicacao)
        db.session.add(novo_livro)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('adicionar_livro.html')

@app.route('/editar_livro/<int:id>', methods=['GET', 'POST'])
def editar_livro(id):
    livro = Livro.query.get_or_404(id)
    if request.method == 'POST':
        livro.titulo = request.form['titulo']
        livro.autor = request.form['autor']
        livro.ano_publicacao = request.form['ano_publicacao']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar_livro.html', livro=livro)

@app.route('/excluir_livro/<int:id>')
def excluir_livro(id):
    livro = Livro.query.get_or_404(id)
    db.session.delete(livro)
    db.session.commit()
    return redirect(url_for('index'))
