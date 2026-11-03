
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to Cloud Computing</title>
    </head>
    <body style="text-align:center;
                 font-family:Arial;
                 background-color:#e6f7ff;
                 padding:50px;">

        <h1>Welcome to Cloud Computing!</h1>
        <h2>Learn. Explore. Innovate.</h2>
        <p>Discover the power of cloud technology.</p>

        <h3>Benefits of Cloud Computing</h3>
        <p>1. Scalability</p>
        <p>2. Cost Efficiency</p>
        <p>3. Flexibility</p>
        <p>4. High Availability</p>
        <p>5. Resource Sharing</p>

    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0",
            port=int(os.environ.get("PORT", 8000)))
