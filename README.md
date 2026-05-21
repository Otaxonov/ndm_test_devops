# X-Forwarded-For NGINX Chain Demo (Flask)

This project demonstrates secure propagation of the `X-Forwarded-For` header through a chain of multiple NGINX reverse proxies to a backend Flask application.

It solves a common DevOps problem:
- preserving full client → proxy chain
- preventing header spoofing
- supporting multiple chained reverse proxies

---

# Project Structure

project/
├── docker-compose.yml
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
├── nginx/
│   ├── nginx1.conf
│   ├── nginx2.conf
│   ├── nginx3.conf

---

# Architecture

Client → nginx1 → nginx2 → nginx3 → Flask app

---

# Run

## 1. Build and start all services

docker-compose up --build

## 2. Check running containers

docker ps

## 3. Access entry point

http://localhost:8081

---

# Testing

## Normal request

curl http://localhost:8081

Expected output:

X-Forwarded-For: client-ip, nginx1, nginx2, nginx3

---

## Spoofing attempt

curl -H "X-Forwarded-For: 1.1.1.1,2.2.2.2" http://localhost:8081

Expected result:
- spoofed IP MUST NOT appear
- only real proxy chain is preserved

---

# Key Idea

## nginx1 (edge / trust boundary)

Removes any client-controlled headers:

proxy_set_header X-Forwarded-For $remote_addr;

---

## nginx2 / nginx3

Appends trusted proxy chain:

proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

---

## Flask app

- reads headers only
- does not trust client input
- prints debug output

---

# Tech Stack

- Docker
- Docker Compose
- NGINX
- Python 3
- Flask

---

# Security Notes

In production use:
- nginx real_ip_module
- trusted proxy CIDRs
- RFC 7239 Forwarded header
- WAF / ingress controller validation

---

# Time Spent

~1.5–2 hours (design + implementation + testing)

---

# Request Flow

curl → nginx1 → nginx2 → nginx3 → Flask