from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    characters = json.loads(data)
    return render_template("characters.html", characters=characters["results"])

@app.route("/profile/<id>")
def get_profile(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    profile = json.loads(data)

    origin_url = profile["origin"]["url"]
    origin_response = urllib.request.urlopen(origin_url)
    origin_data = origin_response.read()
    origin = json.loads(origin_data)

    location_url = profile["location"]["url"]
    location_response = urllib.request.urlopen(location_url)
    location_data = location_response.read()
    location = json.loads(location_data)

    return render_template("profile.html", profile=profile, origin=origin, location=location)

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

@app.route("/locations")
def get_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    locations_data = json.loads(response.read())
    locations = locations_data["results"]
    return render_template("locations.html", locations=locations)

@app.route("/location_profile/<int:id>")
def get_location_profile(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    location_data = json.loads(response.read())
    return render_template("location_profile.html", location=location_data)

@app.route("/episodes")
def get_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    episodes_data = json.loads(response.read())
    episodes = episodes_data["results"]
    return render_template("episodes.html", episodes=episodes)

@app.route("/episode/<id>")
def get_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url)
    episode_data = json.loads(response.read())
    return render_template("episode.html", episode=episode_data)

if __name__ == "__main__":
    app.run(debug=True)
