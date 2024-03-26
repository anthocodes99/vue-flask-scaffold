Flask Vue App
---
Deploy a Vue frontend WITH a Flask backend. 

### Why?
- You want to run more complex server-side business logics.
- You want to connect to a database.
- The package you are relying on are Python-based.
- You need an authentication backend.

### Why not just run 2 separate services?
This guide is specifically for when you want to run both backend and frontend as 1 single service. This is useful for services like Heroku's [Dyno](https://www.heroku.com/dynos) or DigitalOcean's [App Platform](https://www.digitalocean.com/products/app-platform) where it would cost twice as much to have both a front-end and a back-end service.

### Why NOT?
- We have [Nuxt](https://nuxt.com/), which can run server-side logic and authentication.
- You can also run [ExpressJS](https://expressjs.com/) and do the MEVN stack instead.

### How does this work?


#### For deployment
Run the following line to compile and build the frontend application
```sh
$ make build
```
This will create a folder `dist` on the root directory.

We can then deploy the application as a Python Flask application, ultimately calling the service `TODO:`