


from flask import Flask, render_template
import mysql.connector



app = Flask(__name__)

# MySQL database connection
#mydb = mysql.connector.connect(
  #  hostname="db-healthbuddy.mysql.database.azure.com",  # Replace with your MySQL host
  #  user="Admin123",  # Replace with your MySQL username
  #  password="Pranaya211",  # Replace with your MySQL password
   # database="medBuddy"  # Replace with your MySQL database name
#)

#mydb = mysql.connector.connect(
 #   host="health-db.mysql.database.azure.com",
 #   user="User1234",
 #   port="3306",
 #   password="Admin@123",
   # database="medBuddy"
#)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/')
#def submit():
 #    if request.method == 'POST':

   #   full_name = request.form['Full_Name']
   #   phone_number = request.form['Phone_Number']
   #   email = request.form['Email']
   #   disease = request.form['Disease']
   #   message = request.form['Message']

     # Create a cursor
   #   cur = mydb.cursor()

     # Execute MySQL command
   #   cur.execute("INSERT INTO your_table_name(full_name, phone_number, email, disease, message) VALUES(%s, %s, %s, %s, %s)",
   #                 (full_name, phone_number, email, disease, message))

     #  Commit changes to the database
   #  mydb.commit()

      #   Close the connection
   #  cur.close()

   #  return 'Form submitted successfully'


#@app.route('/about',methods=['GET'])
#def about():
#   return render_template('about.html')



#@app.route('/services',methods=['GET'])
#def services():
 #  return render_template('services.html')




#@app.route('/contact')
#def contact():
 #   return render_template('contact.html')

 #   name = request.form['w3lName']
  #  email = request.form['w3lSender']
  #  subject = request.form['w3lSubject']
   # message = request.form['w3lMessage']

  #  try:
   #     with mydb.cursor() as cursor:
    #        sql = "INSERT INTO messages (name, email, subject, message) VALUES (%s, %s, %s, %s)"
      #      cursor.execute(sql, (name, email, subject, message))
      #      mydb.commit()
       #     return 'Form submitted successfully and data saved to the database!'
   # except Exception as e:
   #     return str(e)
            



#@app.route('/healthbot')
#def healthbot():
 #  return render_template('healthbot.html')





if __name__ == '__main__':
    app.run(debug=True)
    



