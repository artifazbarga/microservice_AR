from services import root_dir, nice_json
from flask import Flask ,redirect ,render_template,url_for,session
import query ,os ,datetime


from werkzeug.exceptions import NotFound


app = Flask(__name__)

app.secret_key = os.urandom(24)


@app.route("/getbooking/<uid>")
def bookings_list(uid):
    session['uid']=uid
    return query.querydatabasebyID("bookings", "bookinglist.html",uid)+"<br><a href='/' >Home Page</a><br>"


@app.route("/addbooking/<mid>/<uid>", methods=['GET', 'POST'])
def add_booking(mid,uid):
    query.Insbooking("bookings", (mid, uid,datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    return redirect("/getbooking/"+uid)

#
# @app.route("/", methods=['GET'])
# def hello():
#     return nice_json({
#         "uri": "/",
#         "subresource_uris": {
#             "bookings": "/bookings",
#             "booking": "/bookings/<username>"
#         }
#     })
#
#
# @app.route("/bookings", methods=['GET'])
# def booking_list():
#     return nice_json(bookings)


# @app.route("/bookings/<username>", methods=['GET'])
# def booking_record(username):
#     if username not in bookings:
#         raise NotFound
#
#     return nice_json(bookings[username])

if __name__ == "__main__":
    app.run(port=5003, debug=True)

