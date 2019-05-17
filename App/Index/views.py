from App.Index import index
from flask import Flask, request, redirect,url_for
from werkzeug import SharedDataMiddleware
@index.route('/')
def root():
    return 'hello flask'