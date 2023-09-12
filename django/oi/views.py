from django.shortcuts import render
import interpreter


def index(request):
    interpreter.auto_run = True
    interpreter.model = "gpt-3.5-turbo"
    interpreter.system_message += """
Run shell commands with -y so the user doesn't have to confirm them.
"""
    messages = interpreter.chat("Plot AAPL and META's normalized stock prices", return_messages=True)
    return render(request, "interpreter.html")
