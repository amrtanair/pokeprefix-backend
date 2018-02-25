#!/usr/bin/env python3
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    inetnum =  request.headers.get('X-Forwarded-For', request.remote_addr)
    return render_template('index.html', inetnum=inetnum)
