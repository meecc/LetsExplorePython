#!/usr/bin/env python
# coding=utf-8
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/questions.sqlite'

db = SQLAlchemy(app)


class Topics(db.Model):
    __tablename__ = "topics"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    questions = relationship("Questions", back_populates="topics")


class Questions(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    topics_id = db.Column(db.Integer, ForeignKey('topics.id'))
    topics = relationship("Topics", back_populates="questions")
    choices = relationship("Choice", back_populates="questions")


class Choice(db.Model):
    __tablename__ = "choice"
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, ForeignKey('questions.id'))
    questions = relationship("Questions", back_populates="choices")
    choice = db.Column(db.String)
    correct = db.Column(db.Boolean)


def get_topics():
    result = Topics.query.with_entities(Topics.name).all()
    result = [r for r, in result]
    print(result, flush=True)
    return result


@app.route("/")
def home():
    topics = Topics.query.with_entities(Topics.name).all()
    topics = [r for r, in topics]
    print(topics)
    return render_template("index.html", topics=topics)


@app.route("/start_one_q", methods=["GET"])
def start_one_q():
    if request.args.get("topic", "null"):
        topic_id = request.args.get("topic")
        no = 5
        # Lets get random 5 questions from the topic and start working on it.
        questions = Questions.query.order_by(func.random()).with_entities(Questions.id).filter(
            Questions.topics_id == topic_id).limit(no)
        for q in questions:
            print(q)
    return redirect(url_for("one_q", test="test", quest=10, topics=23))


@app.route("/one_q", methods=['GET'])
def one_q():
    print(request.args)
    q_id = request.args.get("q_id")
    question = Questions.query.filter(Questions.id == q_id).first()

    return render_template("one_q.html", question=question)


@app.route("/start_quiz", methods=['GET'])
def start_quiz():
    no = 5
    topic_id = request.args.get('topic')
    print(topic_id)
    questions = Questions.query.order_by(
        func.random()).with_entities(Questions.id).filter(
        Questions.topics_id == topic_id).limit(no)
    print(questions)
    quest = []
    for q in questions:
        quest.append(q[0])
    print(quest)
    return render_template("start_quiz.html", questions=quest)


@app.route("/show_result", methods=['POST'])
def show_result():
    selections = request.form
    correct_answers = 0
    for k, v in selections.items():
        if k.startswith("choice_"):
            print(Choice.query.filter(Choice.id == v).first().id)
            if Choice.query.filter(Choice.id == v).first().correct == 1:
                correct_answers += 1
            print(k, v)
    return "Thanks a lot:<br>Total correct Answers= " + str(correct_answers)


if __name__ == "__main__":
    app.run(debug=True)
    # print(get_topics())
