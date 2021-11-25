# gh-hops and Flask

Use the latest Python in Grasshopper, including libraries such as Numpy and SciPy. [More info](https://developer.rhino3d.com/guides/grasshopper/hops-component/#calling-a-cpython-server)

## Setup

### As VS Code Development Container (recommended)

Requirements: 
- [Visual Studio Code](https://code.visualstudio.com/)
- [Remote Containers Addon](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)

1. Clone this repository
2. Make sure Docker is running
3. Open the folder in VS Code
4. Choose "Remote Containers: Open Folder in Container" (The command panel is invoked with `f1`)

### Do it yourself 
With venv, pip, etc. like any other Python dev environment

## How To

1. Add your functions to app.py
2. Run the Server: `python app.py`, it will log something like `[INFO]  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)` to the console.
3. Add a Hops Component to your Grasshopper definitions (you may need to install it with the `Package Manager` in Rhino)
4. Double click the Hops Component on the Canvas. Enter the path to your function in the Pop Up. (In our example it would be `http://127.0.0.1:5000/[your function here	]`)

