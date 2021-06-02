import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from  sqlalchemy.sql.expression import func

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_question = questions[start:end]
    return current_question

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)


  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


  @app.after_request
  def after_request(response):
      response.headers.add(
          "Access-Control-Allow-Headers", "Content-Type, Authorization, true"
      )
      response.headers.add(
          "Access-Control-Allow-Methods", "GET, PUT, PATCH, POST, DELETE, OPTIONS")

      return response


  @app.route("/categories")
  def retrieve_categories():
      categories = Category.query.order_by(Category.id).all()
      disc_categories = {category.id: category.type for category in categories}
      if len(categories) == 0:
          abort(404)
      return jsonify(
          {
              "succes": True,
              "total_categories": len(categories),
              "categories": disc_categories,
              "current_category": None
          }
      )


  @app.route("/questions")
  def retrieve_questions():
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      #Categories
      categories = Category.query.order_by(Category.id).all()
      disc_categories = {category.id: category.type for category in categories}


      if len(current_questions) == 0:
          abort(404)
      return jsonify(
          {
       "success": True,
       "questions": current_questions,
       "total_questions": len(Question.query.all()),
       "categories": disc_categories,
       "current_category":None

      }
      )



  @app.route("/questions/<question_id>", methods=["DELETE"])
  def delete_book(question_id):
      error = True
      try:
          question = Question.query.get(question_id)
          db.session.delete(question)
          db.session.commit()

      except:
          error = False
          db.session.rollback()
          abort(405)
      finally:
          db.session.close()

      return jsonify(
          {"success": error,
           "deleted": int(question_id),
           "total_questions": len(Question.query.all())}
      )


  @app.route("/questions", methods=["POST"])
  # @cross_origin()
  def create_question():
      body = request.get_json()

      new_questions = body.get('question', None)
      new_answer = body.get('answer', None)
      new_category = body.get('category', None)
      new_difficulty = body.get('difficulty', None)

      try:
          question = Question(question=new_questions, answer=new_answer, category=new_category, difficulty=new_difficulty)
          question.insert()


          return jsonify({
              'success': True,
              'created': question.id,
              'total_questions': len(Question.query.all())
          })
      except:
          abort(405)



  @app.route("/questions/search", methods=["POST"])
  # @cross_origin()
  def search_question():
      body = request.get_json()
      search = body.get('searchTerm', None)
      selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search)))
      current_questions = paginate_questions(request, selection)

      return jsonify({
          'success': True,
          'questions': current_questions,
          'total_questions': len(selection.all()),
          'current_category': None
      })



  @app.route("/categories/<int:id>/questions")
  def retrieve_question_based_on_category(id):
      category = Category.query.filter_by(id=id).first_or_404()
      selection = Question.query.filter_by(category = id)
      current_questions = paginate_questions(request, selection)


      if len(current_questions) == 0:
          abort(404)
      return jsonify(
          {
              "success": True,
              "questions": current_questions,
              "total_questions": len(Question.query.all()),
              "current_category": category.type

          }
      )



  @app.route("/quizzes", methods=["POST"])
  # @cross_origin()
  def quizz():
      try:
          body = request.get_json()
          previous_question = body.get('previous_questions', None)
          quiz_category = body.get('quiz_category', None)
          if previous_question:
              resultado = Question.query.filter(Question.category==quiz_category['id'], Question.id != previous_question[0]).all()
              result = random.choice(resultado).format()
          else:
              result = Question.query.order_by(func.random()).filter_by(category=quiz_category['id']).first_or_404().format()
          return jsonify(
              {
                  "success": True,
                  "question": result

              }
          )
      except:
          abort(404)


  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "Not found"
      }) , 404

  @app.errorhandler(422)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "Unprocessable Entity"
      }), 422

  @app.errorhandler(405)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 405,
          "message": "Method not allowed"
      }), 405

  return app

    