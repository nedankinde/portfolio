## Bulid container using Podman
```
podman build -t flask-app .
```

## Run container using Podman (Detached Mode)
```
podman run -d -p 5000:5000 flask-app
```

#### Or run with "flask" command

```
# pipx install flask
flask --app main run --port=8080
```

## Clean up
```
podman image rm flask-app
```