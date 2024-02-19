from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters = dict["results"])


@app.route("/profile/<id>")
def get_profile(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    profile_dict = json.loads(data)

    origin_url = profile_dict["origin"]["url"]
    origin_response = urllib.request.urlopen(origin_url)
    origin_data = origin_response.read()
    origin_dict = json.loads(origin_data)

    location_url = profile_dict["location"]["url"]
    location_response = urllib.request.urlopen(location_url)
    location_data = location_response.read()
    location_dict = json.loads(location_data)

    return render_template("profile.html", profile=profile_dict, origin=origin_dict, location=location_dict)

@app.route("/lista")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        }

        characters.append(character)
    
    return {"characters": characters}
#Verificar aqui no locations
@app.route("/locations.html")
def get_locations():
    url = "https://rickandmortyapi.com/api/location"
    response_data = urllib.request.urlopen(url)
    data = json.loads(response_data.read())

    locations_data = []

    for location in data["results"]:
        id = location["id"]
        name = location["name"]
        dimension = location["dimension"]
        type = location["type"]
        locations_data.append({"id": id, "name": name, "dimension": dimension, "type": type})
    return render_template("locations.html", locations=locations_data)

#Verificar aqui no location
@app.route("/location/<id>")
def get_list_locations():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    locations_data = response.read()
    locations_dict = json.loads(locations_data)

    locations_list = locations_dict["results"]
    
    return render_template("locations.html", locations=locations_list)

@app.route("/location_profile/<int:id>")
def get_location_profile(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    location_data = response.read()
    location_dict = json.loads(location_data)

    return render_template("location_profile.html", location=location_dict)

@app.route("/episodes")  

def get_list_episodes_page():
    url = "https://rickandmortyapi.com/api/episode" 
    response = urllib.request.urlopen(url)  
    episodes = response.read()  
    dict = json.loads(episodes) 

    return render_template("episodes.html", episodes = dict["results"]) 


@app.route("/listepisodes")

def get_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url) 
    episodes = response.read() 
    dict = json.loads(episodes) 
    episodes = [] 
    
    for episode in dict["results"]: 
        episode = {  
            "episode":episode["episode"],
            "name":episode["name"],
            "air_date":episode["air_date"],
            "id":episode["id"]
        }        
        episodes.append(episode) 

    return {"episodes":episodes} 


@app.route("/episode/<id>") 

def get_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url) 
    data = response.read(); 
    episode_dict = json.loads(data)
    
    return render_template("episodes.html", episode=episode_dict) 


