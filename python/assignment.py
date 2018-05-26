from flask import Flask

from flask import request

app=Flask(__name__)

@app.route('/grader')

def grader(mark =0, grade= 'nul'):

  mark =int(request.args.get('mark,mark'))


if marks >71:
 return'A'
 
elif marks >61:

 return'B'

elif mark >51:
 return 'c'
else:
   return 'D'

   return "mark of {} is {}".format(marks, total_marks)
   if __name__=='__main__':
 app.run (host='0.0.0.0',port=8080)