# Reverse Proxy

### 🔁 Reverse Proxy – bu nima?
Reverse Proxy bu — Nginx foydalanuvchidan so‘rovni oladi va uni boshqa backend serverga (masalan, Flask, FastAPI, Node.js) yuboradi, so‘ng javobni qaytaradi.


---

## 📁 Loyiha tuzilmasi:

```
docker-nginx/
├── conf.d/
│   └── app.conf         <-- Nginx konfiguratsiya
├── docker-compose.yml   <-- Docker Compose
└── Dockerfile           <-- Nginx Dockerfile
```

---

## 🚀 Ishga tushurish:

Terminalda quyidagilarni bajar:

```bash
cd docker-nginx
docker-compose up --build -d
```

---

## 🔍 Test qilish:

Brauzerda:

* `http://localhost:9001` → `You have reached Application 1`
* `http://localhost:9002` → `You have reached Application 2`

---

## ✅ Best Practice Xususiyatlari:

| Narsa                      | Sababi                               |
| -------------------------- | ------------------------------------ |
| `nginx:alpine`             | Eng yengil va xavfsiz rasm           |
| `COPY conf.d/app.conf ...` | Statik konfiguratsiyani ichga olish  |
| `docker-compose.yml`       | Loyihani boshqarish soddalashadi     |
| `restart: unless-stopped`  | Xizmat avtomatik qayta ishga tushadi |

---
