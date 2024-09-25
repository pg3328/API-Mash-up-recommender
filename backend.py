import dbconnection
from flask import Flask, request, render_template

client = dbconnection.get_the_connection()
app = Flask(__name__)


def query1(update_year,protocol,lower_rating,upper_rating,tags):
    update_year='^'+update_year
    query = {"dateModified": {"$regex": update_year}, "protocols": protocol, "rating": {"$gt": lower_rating, "$lt": upper_rating},
             "tags": {"$in": tags}}
    db = client["programmable_web"]
    api_data = db["api_collection"]
    result = api_data.find(query)
    api_names = [doc['name'] for doc in result]
    return api_names


def query2(update_year,lower_rating,upper_rating,tags,apis):
    update_year = "^"+update_year
    query = {"updated": {"$regex": update_year}, "rating": {"$gt": lower_rating, "$lt": upper_rating}, "tags": {"$in": tags},
             "apis": {"$in": apis}}
    db = client["programmable_web"]
    api_data = db["mashup_collection"]
    result = api_data.find(query)
    mashup_names = [doc['name'] for doc in result]
    return mashup_names


def search_api_by_keywords(keywords):
    client = dbconnection.get_the_connection()
    db = client["programmable_web"]
    api_data = db["api_collection"]

    query = {"$and": []}
    for keyword in keywords:
        query["$and"].append({"$or": [
            {"title": {"$regex": f".*{keyword}.*", "$options": "i"}},
            {"summary": {"$regex": f".*{keyword}.*", "$options": "i"}},
            {"description": {"$regex": f".*{keyword}.*", "$options": "i"}}
        ]})

    result = api_data.find(query)
    api_names = [doc["name"] for doc in result]
    return api_names


def search_mashup_by_keywords(keywords):
    client = dbconnection.get_the_connection()
    db = client["programmable_web"]
    mashup_data = db["mashup_collection"]
    query = {"$and": []}
    for keyword in keywords:
        query["$and"].append({"$or": [
            {"title": {"$regex": f".*{keyword}.*", "$options": "i"}},
            {"summary": {"$regex": f".*{keyword}.*", "$options": "i"}},
            {"description": {"$regex": f".*{keyword}.*", "$options": "i"}}
        ]})

    result = mashup_data.find(query)
    mashup_names = [doc["name"] for doc in result]
    return mashup_names


@app.route("/", methods=["GET", "POST"])
def home():

    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    my_request = request.form.get("request")
    my_service = request.form.get("service")
    if my_request == "keyword":
        my_keywords = request.form.get("keywords")
        my_keywords = my_keywords.split(',')
        if my_service == "mashup":
            name = search_mashup_by_keywords(my_keywords)
            return render_template("index.html", names=name)
        else:
            name = search_api_by_keywords(my_keywords)
            return render_template("index.html", names=name)
    else:
        my_updated_year = request.form.get("updated-year")
        my_rating = request.form.get("rating")
        my_rating = my_rating.split('-')
        my_tags = request.form.get("tags")
        my_tags = my_tags.split(',')
        if my_service == "mashup":
            my_apis = request.form.get("apis")
            my_apis = my_apis.split(',')
            name = query2(my_updated_year, float(my_rating[0]), float(my_rating[1]), my_tags, my_apis)
            return render_template("index.html", names=name)
        else:
            my_protocol = request.form.get("protocols")
            name = query1(my_updated_year, my_protocol, float(my_rating[0]), float(my_rating[1]), my_tags)
            return render_template("index.html", names=name)




if __name__ == '__main__':
    app.run(debug=True)
