from flask import Flask , render_template , jsonify

app = Flask(__name__)

JOBS = [
          {
            'id': 1 ,
            'title':"Data Analysis",
            'location':"Lahore",
            'salary':"10,0000"
               
          },
          {  
            'id': 2 ,
            'title':"Graphic Desinger",
            'location':"Lahore",
            'salary':"15,0000"
    
     
          },
            
          {
            'id':3 ,
            'title':"Programmer",
            'location':"remote",
            

          },

          {
            'id': 4 ,
            'title':"DB Administrator",
            'location':"Lahore",
            'salary':"20,0000"

          }
  
      ]



@app.route('/')
def hello_world():
  return render_template('home.html', jobs =JOBS, compnay_name ='Iubian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host= '0.0.0.0' , debug= True)
