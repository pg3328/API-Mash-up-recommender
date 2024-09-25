import pymongo
from urllib.parse import quote_plus

client_id = 'mongodb+srv://pg3328:room919@N@programmingweb.2jrqleo.mongodb.net/?retryWrites=true&w=majority'
username = "pg3328"
password = "xxxxxx"
client_id = client_id.replace(username, quote_plus(username))
client_id = client_id.replace(password, quote_plus(password))


def insert_data(mycollection, data_to_be_inserted):
    mycollection.insert_many(data_to_be_inserted)


def read_mashup_data(filename):
    """
    Read the mashup data from the file
    :param filename: The name of the file to read
    :return: The JSON object containing the mashup data
    """
    with open(filename, 'r', encoding="ISO-8859-1") as f:
        lines = f.readlines()

    mashup_records = []

    for line in lines:
        fields = line.strip().split('$#$')
        api_used=[]
        api_links=[]
        for apis in fields[16].split('###'):
            api_split = apis.split('$$$')
            api_used.append(api_split[0])

        rating = float(fields[3]) if fields[3] else 0.0
        mashup_record = {
            'id': fields[0],
            'title': fields[1],
            'summary': fields[2],
            'rating': rating,
            'name': fields[4],
            'label': fields[5],
            'author': fields[6],
            'description': fields[7],
            'type': fields[8],
            'downloads': fields[9],
            'useCount': fields[10],
            'sampleUrl': fields[11],
            'dateModified': fields[12],
            'numComments': fields[13],
            'commentsUrl': fields[14],
            'tags': fields[15].split('###'),
            'apis': api_used,
            'updated': fields[17]
        }
        mashup_records.append(mashup_record)
    return mashup_records


def read_api_data(filename):
    """
    Read the API data from the file
    :param filename: The name of the file to read
    :return: The JSON object containing the API data
    """
    with open(filename, 'r', encoding="ISO-8859-1") as f:
        lines = f.readlines()

    api_records = []


    for line in lines:
        fields = line.strip().split('$#$')
        rating = float(fields[3]) if fields[3] else 0.0
        api_record = {
            'id': fields[0],
            'title': fields[1],
            'summary': fields[2],
            'rating': rating,
            'name': fields[4],
            'label': fields[5],
            'author': fields[6],
            'description': fields[7],
            'type': fields[8],
            'downloads': fields[9],
            'useCount': fields[10],
            'sampleUrl': fields[11],
            'downloadUrl': fields[12],
            'dateModified': fields[13],
            'remoteFeed': fields[14],
            'numComments': fields[15],
            'commentsUrl': fields[16],
            'tags': fields[17].split('###'),
            'category': fields[18],
            'protocols': fields[19],
            'serviceEndpoint': fields[20],
            'version': fields[21],
            'wsdl': fields[22],
            'dataFormats': fields[23],
            'apiGroups': fields[24],
            'example': fields[25],
            'clientInstall': fields[26],
            'authentication': fields[27],
            'ssl': fields[28],
            'readonly': fields[29],
            'VendorApiKits': fields[30],
            'CommunityApiKits': fields[31],
            'blog': fields[32],
            'forum': fields[33],
            'support': fields[34],
            'accountReq': fields[35],
            'commercial': fields[36],
            'provider': fields[37],
            'managedBy': fields[38],
            'nonCommercial': fields[39],
            'dataLicensing': fields[40],
            'fees': fields[41],
            'limits': fields[42],
            'terms': fields[43],
            'company': fields[44],
            'updated': fields[45]
        }

        api_records.append(api_record)

    return api_records


def get_the_connection():
    return pymongo.MongoClient(client_id)


def main():
    myclient = get_the_connection()
    production = myclient.programmable_web
    # api_collection = production.api_collection
    # api_data = read_api_data("api.txt")
    # insert_data(api_collection, api_data)
    mashup_collection = production.mashup_collection
    mashup_data = read_mashup_data("mashup.txt")
    insert_data(mashup_collection, mashup_data)

