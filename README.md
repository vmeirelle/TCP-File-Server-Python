# TCP File Server
## Description

This repository contains a simple TCP IPv4 server that allows file retrieval via a web browser. Users can access the server by navigating to `localhost:9999` (or specifying a custom host and port) and requesting files from the `/data` folder. The project was developed as part of a Computer Networks assignment at UFRB (Federal University of Recôncavo da Bahia).

## Project Overview

- The server listens for incoming connections.
- Upon connection, it receives requests from web browsers.
- Users can request files by specifying their paths.
- The server retrieves the requested files (e.g., HTML, images, videos) from the `/data` folder.
- If a requested file is not found, the server returns a 404 error page.

