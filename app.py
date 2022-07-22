from flask import Flask, render_template
import redis


app = Flask(__name__)
redis_client = redis.Redis(host="localhost", port=6379, db=0)


images = [
    "https://3c1703fe8d.site.internapcdn.net/newman/gfx/news/hires/2016/580e2c6ce2919.jpg",
    "https://i.pinimg.com/originals/5e/9c/9c/5e9c9c47a2032739b24d1616526fa77b.jpg",
    "https://i.pinimg.com/originals/fa/7a/b2/fa7ab28ac07477789fbe3f8c25bd8d1a.jpg",
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/cef79a6a-ea95-461b-9629-5510aa6ab42a/d1qwcqm-fac2c4cc-fde3-4d69-beef-c538848feb74.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTpmaWxlLmRvd25sb2FkIl0sIm9iaiI6W1t7InBhdGgiOiIvZi9jZWY3OWE2YS1lYTk1LTQ2MWItOTYyOS01NTEwYWE2YWI0MmEvZDFxd2NxbS1mYWMyYzRjYy1mZGUzLTRkNjktYmVlZi1jNTM4ODQ4ZmViNzQucG5nIn1dXX0.db4Vd9kATKXN7tqxWx3XW2-tl3HiH2ZHkrjCtW0EN0w",
    "https://steemitimages.com/DQmXaiEP2fLDZmP1AdUFx6AEdXRf7BBHADLkWksnFNy8gxR/P1060526.jpg",
    "https://i.ytimg.com/vi/sLKg45mwY84/maxresdefault.jpg",
    "https://i.pinimg.com/originals/ac/59/9f/ac599f5fc8c13cf7d0e16fa704d1b3ee.jpg",
    "https://live.staticflickr.com/5605/15373850999_db0088c226_b.jpg",
    "https://i.pinimg.com/originals/a0/f7/03/a0f70395d512d144c29ce8dc90fe003f.jpg",
    "https://i.pinimg.com/originals/b6/44/9b/b6449b53f19758217f300c30cf71888b.jpg",
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/022147e7-be24-45c8-9cc4-7c35b73a3564/dwc8sx-1f4d865e-2153-4315-bc9b-65affdc9c11a.jpg/v1/fill/w_900,h_642,q_75,strp/random_clouds_sunset_by_radiant0.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl0sIm9iaiI6W1t7InBhdGgiOiIvZi8wMjIxNDdlNy1iZTI0LTQ1YzgtOWNjNC03YzM1YjczYTM1NjQvZHdjOHN4LTFmNGQ4NjVlLTIxNTMtNDMxNS1iYzliLTY1YWZmZGM5YzExYS5qcGciLCJ3aWR0aCI6Ijw9OTAwIiwiaGVpZ2h0IjoiPD02NDIifV1dfQ.gc0N7eJjt0sjOmytT0DeTEYn8VbNl4QJAQa7zchifqI",
    "https://i.pinimg.com/originals/bd/89/84/bd898438c5f01de46babf603f40a401c.jpg",
    "https://i.pinimg.com/originals/c8/d3/d8/c8d3d8dc8c958835099af41e1ad0608b.jpg",
    "https://live.staticflickr.com/3707/13457516364_f3e770c03e_b.jpg",
    "https://i.pinimg.com/originals/bf/ef/c2/bfefc2cdb6510e312307ce6e736f674e.jpg"
]
@app.route('/')
def index():
    url = images[1]
    url = redis_client.get('url')
    if images[1] is None:
        url = images[1]
    redis_client.set('url', url)
    return render_template("index.html", crap=url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    

    



